import abc
import re
from lxml import etree
from io import StringIO

from value_format import format_value


def is_filter_wheels_filters_tag(tag):
    return tag == 'FilterWheelFilters'


ELEMENT_NAMES_TO_EXTRACT = {'Profile': ['Id', 'Name', 'Description'],
                            'ApplicationSettings': ['SkyAtlasImageRepository', 'SkySurveyCacheDirectory'],
                            'AstrometrySettings': ['Elevation', 'Latitude', 'Longitude'],
                            'CameraSettings': ['Id', 'Gain', 'Offset', 'PixelSize'],
                            'FilterWheelSettings': ['Id'],
                            'FlatDeviceSettings': ['Id'],
                            'FlatWizardSettings': ['DarkFlatCount', 'FlatCount', 'FlatWizardMode',
                                                   'HistogramMeanTarget', 'OpenForDarkFlats'],
                            'FocuserSettings': ['Id', 'AutoFocusExposureTime', 'AutoFocusInitialOffsetSteps',
                                                'AutoFocusStepSize', 'BacklashCompensationModel', 'BacklashOut'],
                            'GnssSettings': ['GnssSource'],
                            'GuiderSettings': ['GuiderName', 'PHD2ProfileId'],
                            'ImageFileSettings': ['FilePath', 'FileType'],
                            'MeridianFlipSettings': ['AutoFocusAfterFlip', 'MinutesAfterMeridian',
                                                     'PauseTimeBeforeMeridian', 'Recenter', 'RotateImageAfterFlip',
                                                     'SettleTime'],
                            'PlanetariumSettings': ['PreferredPlanetarium', 'StellariumHost', 'StellariumPort'],
                            'PlateSolveSettings': ['PlateSolverType', 'ExposureTime', 'BlindSolverType'],
                            'RotatorSettings': ['Id'],
                            'SequenceSettings': ['DefaultSequenceFolder', 'DisableSimpleSequencer',
                                                 'DoMeridianFlip',
                                                 'DoMeridianFlip', 'SequencerTargetsFolder',
                                                 'SequencerTemplatesFolder'],
                            'TelescopeSettings': ['FocalLength', 'FocalRatio', 'Id', 'MountName', 'Name',
                                                  'SettleTime'],
                            'WeatherDataSettings': ['Id']}

FILE_FORMAT_KEYS = ['FilePattern', 'FilePatternBIAS', 'FilePatternDARK', 'FilePatternFLAT']

NAME_SPACE_REGEX = re.compile(r'\s*xmlns(:[^\s>"]+)?="[^"]+"\s*')  # Find all namespace attributes
TYPE_AND_NIL_REGEX = re.compile(r'\s+i:(?:type|nil)="[^"]*"')         # Find all 'type' and 'nil' attributes
A_B_OPEN_TAG_REGEX = re.compile(r'(?<=<)(a:|b:)')                  # Find all '<a:' or '<b:' opening tags
A_B_CLOSE_TAG_REGEX = re.compile(r'(?<=</)(a:|b:)')                # Find all '</a:' or '</b:' closing tags


def parse_profile(profile_file):
    with open(str(profile_file), 'r') as profile:
        profile_txt = profile.read()
        for rg in [NAME_SPACE_REGEX, TYPE_AND_NIL_REGEX, A_B_OPEN_TAG_REGEX, A_B_CLOSE_TAG_REGEX]:
            profile_txt = re.sub(rg, '', profile_txt)

    return etree.parse(StringIO(profile_txt))


class ProfileParser(object):
    __metaclass__ = abc.ABCMeta

    profile_xml = None
    elements_to_extract = []
    profile_xml_dict = {}

    def pretty_print(self, profile_file_name, workbook=None, input_directory=None, output_directory=None):
        self.initialize_profile_xml(profile_file_name)
        simplified_profile = self.pretty_print_simplified_profile(workbook)
        return '\n'.join(simplified_profile)

    def initialize_profile_xml(self, profile_file_name):
        self.profile_xml = parse_profile(profile_file_name)
        self.elements_to_extract = [e for e in list(self.profile_xml.iter()) if
                                    e.tag in ELEMENT_NAMES_TO_EXTRACT.keys()]
        self.build_profile_dict()

    def build_profile_dict(self):
        profile_dict = {}
        for element in self.elements_to_extract:
            tag_names = ELEMENT_NAMES_TO_EXTRACT[element.tag]
            profile_dict[element.tag] = self.build_child_dict(element, tag_names)
        self.profile_xml_dict = profile_dict

    def build_child_dict(self, element, tag_names):
        child_dict = {}
        for child in element:
            tag = child.tag.strip()
            if tag in tag_names:
                child_dict[tag] = format_value(child.text)
            elif is_filter_wheels_filters_tag(tag):
                child_dict["FilterWheelFilters"] = self.build_filter_wheel_filters()
        return child_dict

    def build_filter_wheel_filters(self):
        filter_wheel_settings = self.profile_xml.find('.//FilterWheelFilters')
        filter_wheels = []
        for f in filter_wheel_settings.iter():
            if f.tag == '_name':
                filter_wheels.append(f.text.strip())
        return ', '.join(filter_wheels)

    @abc.abstractmethod
    def pretty_print_simplified_profile(self, workbook):
        pass

    @abc.abstractmethod
    def print_child_element(self, items, tag_names):
        pass
