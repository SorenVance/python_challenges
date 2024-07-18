# nina_profile_extractor.py
from profile_parser_pretty import ProfileParerPretty
from profile_parser_csv import ProfileParerCSV
from profile_parser_xlsx import ProfileParerXLSX


from os import path

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

