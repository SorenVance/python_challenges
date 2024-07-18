import re
import unittest
from json import dumps
from pathlib import Path
from itertools import chain

from profile_parser_csv import ProfileParerCSV
from profile_parser_pretty import ProfileParerPretty
from profile_parser_xlsx import ProfileParerXLSX
from profile_parser import (NAME_SPACE_REGEX, TYPE_AND_NIL_REGEX, A_B_OPEN_TAG_REGEX, A_B_CLOSE_TAG_REGEX,
                            ELEMENT_NAMES_TO_EXTRACT, is_filter_wheels_filters_tag, parse_profile)


class ProfileParseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        for file in (chain(Path('./output/').glob('*'))):
            if file.is_file():
                file.unlink()

    def test_is_filter_wheels_filters_tag(self):
        self.assertTrue(is_filter_wheels_filters_tag('FilterWheelFilters'))
        self.assertFalse(is_filter_wheels_filters_tag('blah'))

    def test_NAME_SPACE_REGEX(self):
        xml = ('<Profile xmlns="http://schemas.datacontract.org/2004/07/NINA.Profile"\n'
               + '         xmlns:i="http://www.w3.org/2001/XMLSchema-instance"></Profile>')
        self.assertEqual('<Profile></Profile>', re.sub(NAME_SPACE_REGEX, '', xml).strip())

    def test_TYPE_AND_NIL_REGEX(self):
        xml = ('<SwitchSettings i:type="SwitchSettings"><a:A i:nil="true"/><SequenceCompleteCommand i:nil="true"/>'
               + '<Filter i:nil="true"/></SwitchSettings>')
        expected = '<SwitchSettings><a:A/><SequenceCompleteCommand/><Filter/></SwitchSettings>'
        self.assertEqual(expected, re.sub(TYPE_AND_NIL_REGEX, '', xml).strip())

    def test_A_B_OPEN_TAG_REGEX(self):
        xml = '<a:A><a:B><a:G><a:R><a:ScA><a:ScB><a:ScG><a:ScR>'
        expected = '<A><B><G><R><ScA><ScB><ScG><ScR>'
        self.assertEqual(expected, re.sub(A_B_OPEN_TAG_REGEX, '', xml).strip())

    def test_A_B_CLOSE_TAG_REGEX(self):
        xml = '</a:A></a:B></a:G></a:R></a:ScA></a:ScB></a:ScG></a:ScR>'
        expected = '</A></B></G></R></ScA></ScB></ScG></ScR>'
        self.assertEqual(expected, re.sub(A_B_CLOSE_TAG_REGEX, '', xml).strip())

    def test_parse_profile(self):
        profile_parser = ProfileParerPretty()

        profile_xml = parse_profile('./input/WO-GT81-0.8_ASI2600_AM5.profile')
        elements_tags_to_extract = [e.tag for e in list(profile_xml.iter()) if e.tag in ELEMENT_NAMES_TO_EXTRACT.keys()]
        for tag in ELEMENT_NAMES_TO_EXTRACT.keys():
            self.assertTrue(tag in elements_tags_to_extract)

    def test_build_profile_xml(self):
        profile_parser = ProfileParerCSV()
        profile_parser.pretty_print('./input/WO-GT81-0.8_ASI2600_AM5.profile')
        actual_dict = profile_parser.profile_xml_dict
        print(dumps(actual_dict))
        self.assertEqual(
            {'Id': 'f6e49505-b720-479b-9bc7-5b47f9f21d4d', 'Name': 'WO-GT81-0.8_ASI2600_AM5', 'Description': None},
            actual_dict.get('Profile'))

    @staticmethod
    def test_pretty_print_simplified_profile():
        profile_parser = ProfileParerPretty()
        profile_xml = profile_parser.pretty_print(
            './input/WO-GT81-0.8_ASI2600_AM5.profile')
        print(profile_xml)

    def test_pretty_print_CSV(self):
        profile_parser = ProfileParerCSV()
        profile_xml = profile_parser.pretty_print(
            '/home/stevek/dev/python_challenges/nina/input/WO-GT81-0.8_ASI2600_AM5.profile')
        print(profile_xml)
        profile_lines = profile_xml.split('\n')[:4]
        self.assertEqual('Profile Information for WO-GT81-0.8_ASI2600_AM5', profile_lines[0])
        self.assertEqual('Profile\tId\tf6e49505-b720-479b-9bc7-5b47f9f21d4d', profile_lines[1])
        self.assertEqual('\tName\tWO-GT81-0.8_ASI2600_AM5', profile_lines[2])
        self.assertEqual('\tDescription\tNone', profile_lines[3])

    def test_pretty_print_XSLX(self):
        profile_parser = ProfileParerXLSX()
        profile_parser.pretty_print(input_directory='./input/', output_directory='./output/')

        file_count = sum(1 for _ in Path('./output/').glob('N.I.N.A. Profiles.xlsx'))
        self.assertEqual(1, file_count)
        output_file = next(Path('./output/').glob('N.I.N.A. Profiles.xlsx'), None)
        self.assertIsNotNone(output_file)
        self.assertTrue(output_file.is_file())


if __name__ == '__main__':
    unittest.main()
