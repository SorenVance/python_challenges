# nina_profile_extractor.py
import abc
import re
from functools import reduce
from io import StringIO
from itertools import chain
from pathlib import Path

import xlsxwriter
from lxml import etree

from os import path


# ==================================================================================================
# ==================================================================================================
def is_float(v):
    return v.replace('-', '', 1).replace('.', '', 1).isdigit()


def is_int(v):
    return v.replace('-', '', 1).isdigit()


def is_exponential(v):
    lc = v.lower()
    if 'e' not in lc or not is_int(lc[-1]):
        return False
    cleaned = reduce(lambda s, r: s.replace(r, ''), ['-', '.', '+', '', 'e'], lc)
    return cleaned.isdigit()


def format_value(v):
    if v is None:
        return None
    if isinstance(v, list):
        return ', '.join(map(str, v))

    stripped = v.strip() if type(v) is str else v
    if is_int(stripped):
        return int(stripped)
    if is_float(stripped):
        return float(stripped)
    return stripped


def space_ify_string(key):
    if key is None:
        return None
    spacey_values = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)', key)
    return ' '.join(spacey_values)


# ==================================================================================================
# ==================================================================================================
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
TYPE_AND_NIL_REGEX = re.compile(r'\s+i:(?:type|nil)="[^"]*"')  # Find all 'type' and 'nil' attributes
A_B_OPEN_TAG_REGEX = re.compile(r'(?<=<)(a:|b:)')  # Find all '<a:' or '<b:' opening tags
A_B_CLOSE_TAG_REGEX = re.compile(r'(?<=</)(a:|b:)')  # Find all '</a:' or '</b:' closing tags


def parse_profile(profile_file):
    with open(str(profile_file), 'r') as profile:
        profile_txt = profile.read()
        for rg in [NAME_SPACE_REGEX, TYPE_AND_NIL_REGEX, A_B_OPEN_TAG_REGEX, A_B_CLOSE_TAG_REGEX]:
            profile_txt = re.sub(rg, '', profile_txt)

    return etree.parse(StringIO(profile_txt))


# ==================================================================================================
# ==================================================================================================
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


# ==================================================================================================
# ==================================================================================================
class ProfileParerPretty(ProfileParser):

    def pretty_print_simplified_profile(self, workbook=None):
        simplified_profile = []
        for key, val in self.profile_xml_dict.items():
            tag_names = ELEMENT_NAMES_TO_EXTRACT[key]
            simplified_profile.append(key)
            simplified_profile.extend(self.print_child_element(val, tag_names))
        return simplified_profile

    def print_child_element(self, items, tag_names):
        child_elements = []
        for key, val in items.items():
            child_elements.append(f"    {key} - {val}")
        return child_elements


# ==================================================================================================
# ==================================================================================================
class ProfileParerCSV(ProfileParser):

    def pretty_print_simplified_profile(self, workbook=None):
        simplified_profile = [f'Profile Information for {self.profile_xml.find("./Name").text.strip()}']
        for key, val in self.profile_xml_dict.items():
            tag_names = ELEMENT_NAMES_TO_EXTRACT[key]
            simplified_profile.append(f"{key}\t{tag_names[0]}\t{val[tag_names[0]]}")
            simplified_profile.extend(self.print_child_element(val, tag_names[1:]))
            simplified_profile.append("\t\t\t")
        return simplified_profile

    def print_child_element(self, items, tag_names):
        child_elements = []
        for tag in tag_names:
            if tag in items.keys():
                child_elements.append(f"\t{tag}\t{items[tag]}")
        return child_elements


# ==================================================================================================
# ==================================================================================================
ALIGN_LEFT = {'align': 'left'}
BG_COLOR_SILVER_ = {'bg_color': 'silver'}
HEADER_TEXT_PARAMS = {'bold': True, 'align': 'center', 'font_size': 24, 'bg_color': 'silver'}


def setup_worksheet(wkbk, sheet_name):
    worksheet = wkbk.add_worksheet(sheet_name)
    worksheet.set_margins(right=0.25, top=0.25, bottom=0.25)
    worksheet.fit_to_pages(1, 1)
    return worksheet


def print_sub_elements(align_left_format, col, row, sub_elements, worksheet):
    for pair in sub_elements:
        worksheet.write_row(row, col + 1, pair, align_left_format)
        row += 1
    return row


class ProfileParerXLSX(ProfileParser):

    def pretty_print(self, profile_name=None, workbook=None, input_directory=None, output_directory=None):
        input_path = Path(input_directory)
        output_file_path = f'{output_directory if output_directory is not None else './output'}/N.I.N.A. Profiles.xlsx'

        with xlsxwriter.Workbook(output_file_path, {'strings_to_numbers': True}) as workbook:
            for file in (chain(input_path.glob('*.profile'))):
                print(f'Processing profile: {file.name}')
                super().pretty_print(file, workbook)

    def pretty_print_simplified_profile(self, workbook):
        profile_name = self.profile_xml.find("./Name").text.strip()
        sheet_name = profile_name.replace(' - ', '_').replace(' ', '_').replace('/', '-')
        worksheet = setup_worksheet(workbook, sheet_name)
        self.print_rows(workbook, worksheet, f'Profile Information for {profile_name}')
        worksheet.autofit()
        return []

    def print_rows(self, wkbk, worksheet, xls_title):
        header_text_format = wkbk.add_format(HEADER_TEXT_PARAMS)
        worksheet.merge_range(0, 0, 0, 2, xls_title, header_text_format)
        align_left_format = wkbk.add_format(ALIGN_LEFT)
        merged_cells_format = wkbk.add_format(BG_COLOR_SILVER_)

        row = 2
        col = 0
        for key, val in self.profile_xml_dict.items():
            tag_names = ELEMENT_NAMES_TO_EXTRACT[key]
            worksheet.write(row, 0, space_ify_string(key), align_left_format)
            sub_elements = self.print_child_element(val, tag_names)
            row = print_sub_elements(align_left_format, col, row, sub_elements, worksheet)
            worksheet.merge_range(row, 0, row, 2, None, merged_cells_format)
            row += 1

        self.print_file_formats(worksheet, row, align_left_format)

    def print_child_element(self, items, tag_names):
        return [[space_ify_string(t), v] for t, v in items.items() if t in items.keys()]

    def print_file_formats(self, worksheet, row, align_left_format):
        for key in FILE_FORMAT_KEYS:
            spacey_key = space_ify_string(key)
            value = self.profile_xml.find(f'.//{key}')
            if value is not None:
                path_and_file_name = value.text.strip()
                last_slash = path_and_file_name.rfind('\\') + 1
                path = path_and_file_name[:last_slash]
                file_name = path_and_file_name[last_slash:]
                worksheet.write(row, 0, spacey_key, align_left_format)
                worksheet.write(row, 1, "Path", align_left_format)
                worksheet.write(row, 2, path, align_left_format)
                worksheet.write(row + 1, 1, "File Name", align_left_format)
                worksheet.write(row + 1, 2, file_name, align_left_format)

                row += 2


# ==================================================================================================
# ==================================================================================================
OUTPUT_TYPES = {1: 'PRETTY', 2: 'CSV', 3: 'XLSX'}


def instantiate_parser(parser_choice):
    print(f'Creating {OUTPUT_TYPES[parser_choice]} output format.')
    if parser_choice == 1:
        return ProfileParerPretty()
    elif parser_choice == 2:
        return ProfileParerCSV()
    elif parser_choice == 3:
        return ProfileParerXLSX()


def get_parser_choice():
    print('AVAILABLE OUTPUT TYPES:\n   ', '\n    '.join(f'{k}: {v}' for k, v in OUTPUT_TYPES.items()))
    input_choice = -1
    while input_choice not in OUTPUT_TYPES.keys():
        input_choice = int(input('Enter your choice (1-3): '))
        if input_choice not in OUTPUT_TYPES.keys():
            print('Invalid choice. Please try again.')
    return input_choice


def ask_for_input_directory():
    input_dir = ''
    while not path.isdir(input_dir):
        input_dir = input('Enter the directory path where your profiles are located: ')
        print(f'    {input_dir} is{'' if path.isdir(input_dir) else ' NOT'} a valid directory.')
    return input_dir


def ask_for_output_directory():
    output_dir = ''
    while not path.isdir(output_dir):
        output_dir = input('Enter the directory path where you want to save the output: ')
        print(f'    {output_dir} is{'' if path.isdir(output_dir) else ' NOT'} a valid directory.')
    return output_dir


choice = get_parser_choice()
parser = instantiate_parser(choice)
input_directory = ask_for_input_directory()
output_directory = ask_for_output_directory()

print()
print()
print('================================================================')
print(f'You Chose the {OUTPUT_TYPES[choice]} output format.')
print(f'You selected to pretty print profiles from the directory: {input_directory}')
print(f'The output will be saved in the directory: {output_directory}')
print('================================================================')
print()
parser.pretty_print(input_directory=input_directory, output_directory=output_directory)
