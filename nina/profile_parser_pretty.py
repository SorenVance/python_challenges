
from profile_parser import ProfileParser, ELEMENT_NAMES_TO_EXTRACT


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
