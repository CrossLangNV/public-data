import os.path
import unittest

from CEFAT4Cities.scripts.parse_translations import Parser, Summary

DIR_TEST = os.path.abspath(os.path.dirname(__file__))


class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = Parser(country=None)

        try:
            self.parser.add_folder(DIR_TEST)
        except:
            pass

    def test_add(self):

        summary = self.parser.summaries[0]

        with self.subTest("content"):
            self.assertEqual("EDozvola - prostorno ureÄenje i graditeljstvo", summary.content)

        with self.subTest("translated_content"):
            self.assertEqual("EDozvola — Spatial ureÄe and construction", summary.translated_content)

        with self.subTest("url"):
            self.assertEqual("https://zagreb.hr/", summary.url)

        with self.subTest("lang_source"):
            self.assertEqual("hr", summary.lang_source)

        with self.subTest("lang_target"):
            self.assertEqual("en", summary.lang_target)

    def test_export(self):

        self.parser.export('test.tmx')


class TestModels(unittest.TestCase):
    def test_summary(self):
        summary = Summary(content='',
                          translated_content='',
                          url='',
                          lang_source='DE',
                          lang_target='EN')

        with self.subTest("lang_source"):
            self.assertEqual("de", summary.lang_source)

        with self.subTest("lang_target"):
            self.assertEqual("en", summary.lang_target)
