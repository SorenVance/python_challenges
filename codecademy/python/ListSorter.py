import unittest


def sort_list(list_to_sort, direction):
    ASC = 'asc'
    DESC = 'desc'
    NONE = 'none'

    return list_to_sort


class ListSorterTests(unittest.TestCase):
    test_list = [5, 6, 1, 7, 3, 9, 2, 8, 4, 10]
    asc_list = list(range(1, 11))
    desc_list = list(range(10, 0, -1))

    ASC = 'asc'
    DESC = 'desc'
    NONE = 'none'

    def test_ListSort_GivenList_ReturnsList(self):
        self.assertEqual(self.test_list, sort_list(self.test_list, self.ASC))

    def test_sort_list_GivenNone_ReturnsList(self):
        self.assertEqual(self.asc_list, sort_list(self.test_list, self.ASC))


if __name__ == '__main__':
    unittest.main()
