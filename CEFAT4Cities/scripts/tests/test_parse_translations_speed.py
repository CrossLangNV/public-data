import os
import unittest

from CEFAT4Cities.scripts import parse_translations
from CEFAT4Cities.scripts.parse_translations import Parser


class TestUserScript(unittest.TestCase):

    def setUp(self) -> None:
        # TODO change as this will only work locally.
        self.DIRECTORY = r"C:\Users\Laurens\Data\C4C\translations\trafilatura_temp\trafilatura"

    def test_main(self, run=True,

                  ):
        """
        Runs the whole script.
        :return:
        """
        if not run:
            # Avoid running this test by accident.
            return

        parse_translations.main(directory=self.DIRECTORY, i_start=2)

    def test_shorter_all(self,
                         timeout=10,  # seconds
                         ):
        self.parser = Parser(country="BE")

        # Koekelare is way too big
        MUNI = 'gerolstein.org'  # Quick
        MUNI = 'herent'
        DIR_MUNICIPALITY = os.path.join(self.DIRECTORY, MUNI)
        assert os.path.exists(DIR_MUNICIPALITY)

        self.parser.add_folder(DIR_MUNICIPALITY)

        summary = self.parser.summaries[0]
