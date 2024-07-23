from profile_parser import ProfileParser, ELEMENT_NAMES_TO_EXTRACT, FILE_FORMAT_KEYS
from pathlib import Path
from itertools import chain
import xlsxwriter
import socket

from value_format import space_ify_string

DEFAULT_TEXT = {'align': 'left', 'font_size': 14}
SMALLER_TEXT = {'align': 'left', 'font_size': 10}
BG_COLOR_SILVER_ = {'bg_color': 'silver'}
HEADER_TEXT_PARAMS = {'bold': True, 'align': 'center', 'font_size': 24, 'bg_color': 'silver'}


def setup_worksheet(wkbk, sheet_name):
    worksheet = wkbk.add_worksheet(sheet_name)
    worksheet.set_margins(right=0.25, top=0.25, bottom=0.25)
    worksheet.fit_to_pages(1, 1)
    worksheet.set_column(0, 0, 20)
    worksheet.set_column(0, 1, 36)
    worksheet.set_column(2, 2, 70)
    return worksheet


def print_sub_elements(align_left_format, col, row, sub_elements, worksheet):
    for pair in sub_elements:
        worksheet.write_row(row, col + 1, pair, align_left_format)
        row += 1
    return row


class ProfileParerXLSX(ProfileParser):

    def pretty_print(self, profile_name=None, workbook=None, input_directory=None, output_directory=None):
        input_path = Path(input_directory)
        host_name = socket.gethostname()
        output_file_path = \
            f'{output_directory if output_directory is not None else './output'}/{host_name} N.I.N.A. Profiles.xlsx'
        with xlsxwriter.Workbook(output_file_path, {'strings_to_numbers': True}) as workbook:
            for file in (chain(input_path.glob('*.profile'))):
                print(f'Processing profile: {file.name}')
                super().pretty_print(file, workbook)

    def pretty_print_simplified_profile(self, workbook):
        profile_name = self.profile_xml.find("./Name").text.strip()
        sheet_name = profile_name.replace(' - ', '_').replace(' ', '_').replace('/', '-')
        worksheet = setup_worksheet(workbook, sheet_name)
        self.print_rows(workbook, worksheet, f'Profile Information for {profile_name}')
        return []

    def print_rows(self, wkbk, worksheet, xls_title):
        header_text_format = wkbk.add_format(HEADER_TEXT_PARAMS)
        worksheet.merge_range(0, 0, 0, 2, xls_title, header_text_format)
        default_text_format = wkbk.add_format(DEFAULT_TEXT)
        smaller_text_format = wkbk.add_format(SMALLER_TEXT)
        merged_cells_format = wkbk.add_format(BG_COLOR_SILVER_)

        row = 1
        col = 0
        for key, val in self.profile_xml_dict.items():
            tag_names = ELEMENT_NAMES_TO_EXTRACT[key]
            worksheet.write(row, 0, space_ify_string(key), default_text_format)
            sub_elements = self.print_child_element(val, tag_names)
            row = print_sub_elements(default_text_format, col, row, sub_elements, worksheet)
            worksheet.merge_range(row, 0, row, 2, None, merged_cells_format)
            worksheet.set_row(row, 4)
            row += 1

        self.print_file_formats(worksheet, row, default_text_format, smaller_text_format)

    def print_child_element(self, items, tag_names):
        return [[space_ify_string(t), v] for t, v in items.items() if t in items.keys()]

    def print_file_formats(self, worksheet, row, default_text_format, smaller_text_format):
        for key in FILE_FORMAT_KEYS:
            spacey_key = space_ify_string(key)
            value = self.profile_xml.find(f'.//{key}')
            if value is not None:
                path_and_file_name = value.text.strip()
                worksheet.write(row, 0, spacey_key, default_text_format)
                worksheet.write(row + 1, 0, f'      {path_and_file_name}', smaller_text_format)
                row += 2
