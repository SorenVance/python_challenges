from profile_parser import ProfileParser, ELEMENT_NAMES_TO_EXTRACT


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

