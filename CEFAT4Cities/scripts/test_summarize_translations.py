import unittest

from CEFAT4Cities.scripts.summarize_translations import get_data


class TestGetData(unittest.TestCase):
    def test_open(self):
        filename = 'C:\\Users\\Laurens\\Data\\C4C\\translations\\trafilatura_temp\\trafilatura\\zagreb.hr\\6f84e35e-8499-452f-bacd-a6636b81d8df.jsonl.translated_en.jsonl'

        data = list(get_data(filename))

        self.assertEqual(len(data), 331)

    def test_parsed(self):
        filename = r"test_6f84e35e-8499-452f-bacd-a6636b81d8df.jsonl.translated_en.jsonl"
        data = list(get_data(filename))

        self.assertEqual(len(data), 331)