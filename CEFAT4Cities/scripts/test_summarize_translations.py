import os
import unittest

from CEFAT4Cities.scripts.summarize_translations import JSONL
from CEFAT4Cities.scripts.utils import Country, get_country


class TestGetData(unittest.TestCase):
    def test_open(self):
        filename = 'C:\\Users\\Laurens\\Data\\C4C\\translations\\trafilatura_temp\\trafilatura\\zagreb.hr\\6f84e35e-8499-452f-bacd-a6636b81d8df.jsonl.translated_en.jsonl'

        data = JSONL(filename)

        self.assertEqual(len(data), 331)

    def test_parsed(self):
        filename = r"test_6f84e35e-8499-452f-bacd-a6636b81d8df.jsonl.translated_en.jsonl"

        data = JSONL(filename)

        self.assertEqual(len(data), 331)


class TestExport(unittest.TestCase):

    def setUp(self) -> None:
        filename = r"test_6f84e35e-8499-452f-bacd-a6636b81d8df.jsonl.translated_en.jsonl"

        self.jsonl = JSONL(filename)

    def test_export(self):
        self.jsonl.export()


class TestParse(unittest.TestCase):
    def setUp(self) -> None:
        self.s_in = '{"id":"74705ff8-4374-544b-922c-d52244265048", "title":"Widmung "Fußweg St.Josef Haus" , "Zufahrt untere Marktstraße 8A", "Zufahrt Reitsporthalle": Stadt Gerolstein - Offiziell", "url":"https://gerolstein.org/de/nachrichten/details-nachrichten/widmung-fussweg-stjosef-haus-zufahrt-untere-marktstrasse-8a-zufahrt-reitsporthalle.html", "translated_content":"NO Internal Server Error"}'

        self.l_in = ['"id":"74705ff8-4374-544b-922c-d52244265048"',
                     '"title":"Widmung "Fußweg St.Josef Haus" , "Zufahrt untere Marktstraße 8A"',
                     '"Zufahrt Reitsporthalle": Stadt Gerolstein - Offiziell"',
                     '"url":"https://gerolstein.org/de/nachrichten/details-nachrichten/widmung-fussweg-stjosef-haus-zufahrt-untere-marktstrasse-8a-zufahrt-reitsporthalle.html"',
                     '"translated_content":"NO Internal Server Error"']

        self.l_desired = ['"id":"74705ff8-4374-544b-922c-d52244265048"',
                          '"title":"Widmung "Fußweg St.Josef Haus" , "Zufahrt untere Marktstraße 8A", "Zufahrt Reitsporthalle": Stadt Gerolstein - Offiziell"',
                          '"url":"https://gerolstein.org/de/nachrichten/details-nachrichten/widmung-fussweg-stjosef-haus-zufahrt-untere-marktstrasse-8a-zufahrt-reitsporthalle.html"',
                          '"translated_content":"NO Internal Server Error"']

        self.d_desired = {"id": "74705ff8-4374-544b-922c-d52244265048",
                          "title": "Widmung \"Fußweg St.Josef Haus\" , \"Zufahrt untere Marktstraße 8A\", \"Zufahrt Reitsporthalle\": Stadt Gerolstein - Offiziell",
                          "url": "https://gerolstein.org/de/nachrichten/details-nachrichten/widmung-fussweg-stjosef-haus-zufahrt-untere-marktstrasse-8a-zufahrt-reitsporthalle.html",
                          "translated_content": "NO Internal Server Error"}

    def test_parse_json(self):
        """
        Convert string to dictionary
        :return:
        """

        d = JSONL.parse_json(self.s_in)

        self.assertDictEqual(self.d_desired, d)


class TestFoo(unittest.TestCase):
    """
    all tests without a place
    """

    def setUp(self) -> None:
        filename = 'C:\\Users\\Laurens\\Data\\C4C\\translations\\trafilatura_temp\\trafilatura\\zagreb.hr\\6f84e35e-8499-452f-bacd-a6636b81d8df.jsonl.translated_en.jsonl'

        self.data = JSONL(filename)

    def test_foo(self):

        self.data.export('test.json')

        self.assertEqual(0, 1)

    def test_get_countries(self):

        dir_municipalities = r"C:\Users\Laurens\Data\C4C\translations\trafilatura_temp\trafilatura"

        for municipality in os.listdir(dir_municipalities):

            dir_municipality = os.path.join(dir_municipalities, municipality)

            if not os.path.isdir(dir_municipality) or municipality == "export":
                continue

            country = get_country(municipality=municipality)

            with self.subTest(municipality):
                self.assertIsInstance(country, Country)

            for _ in []:
                pass
