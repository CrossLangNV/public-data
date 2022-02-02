import os.path
import unittest

from CEFAT4Cities.scripts.parse_translations import Parser

DIR_TEST = os.path.abspath(os.path.dirname(__file__))


class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = Parser(country=None)

    def test_add(self):
        try:
            self.parser.add_folder(DIR_TEST)
        except:
            pass

        summary = self.parser.summaries[0]

        with self.subTest("content"):
            self.assertEqual("EDozvola - prostorno ureÄenje i graditeljstvo", summary.content)

        with self.subTest("translated_content"):
            self.assertEqual("EDozvola — Spatial ureÄe and construction", summary.translated_content)
