"""
Script that converts all the available data to tmx.
"""
import glob
import os
import warnings
from typing import Optional

from pydantic import BaseModel

from CEFAT4Cities.scripts.summarize_translations import filter_translated_json, get_orig, JSONL, TranslationError
from CEFAT4Cities.scripts.utils import clean_newlines, Country, get_country


def filter_municipality_by_country(municipality, country: Country):
    """


    :param directory:
    :param country:
    :return:
    """

    return get_country(municipality) == country


def get_municipalities_by_country(directory, country: Country):
    """
    return directories/municipalities belonging to a country.
    """

    return filter(lambda municipality: get_country(municipality) == country, os.listdir(directory))


class PageTrans(BaseModel):
    id: str
    title: str
    url: str
    translated_content: str


class PageOrig(BaseModel):
    url: str
    title: str
    website: str
    content_html: str
    date: str
    language: str
    task: Optional[str]
    id: str
    date_last_update: str


class Summary(BaseModel):
    content: str
    translated_content: str


class Parser:
    def __init__(self, country):
        self.country = country

        self.summaries = []

    def add_folder(self, directory: str):
        """

        :param dir: Path to directory with translation jsons.
        :return:
        """
        # TODO

        # Go over translated jsons.
        for filename_translated_json in filter(filter_translated_json, os.listdir(directory)):

            filename_orig = get_orig(filename_translated_json)

            if not os.path.exists(filename_orig):
                warnings.warn(f"Could not find file: {filename_orig}", UserWarning)

            filename_translated_json
            filename_orig

            data_trans = JSONL(filename_translated_json)

            data_orig = JSONL(filename_orig)

            for d in data_trans:
                if isinstance(d, TranslationError):
                    continue

                page_trans = PageTrans(**d)

                def match_page_orig(data_orig, id) -> PageOrig:
                    """

                    :param data_orig:
                    :param id: from page trans
                    :return:
                    """
                    for d_orig in data_orig:
                        if d_orig["id"] == id:
                            return PageOrig(**d_orig)

                def get_content():
                    b = 0
                    if b:
                        page_orig = match_page_orig(data_orig, page_trans.id)
                    else:
                        # Get from f"{id}_{lang_code}.txt."

                        endPaths = glob.glob(directory + f"/{page_trans.id}_??.txt")
                        if len(endPaths) != 1:
                            warnings.warn(f"Expected only 1 match: {endPaths}")

                        fn_txt_orig = endPaths[0]
                        with open(fn_txt_orig, 'r', encoding="utf8") as file:
                            data = file.read()

                    content = clean_newlines(data)
                    return content

                summary = Summary(content=get_content(),  # TODO retrieve original content
                                  translated_content=clean_newlines(page_trans.translated_content))

                self.summaries.append(summary)


def main(directory):
    for country in Country:

        parser = Parser(country=country.value)

        for municipality in get_municipalities_by_country(directory, country):
            dir_municipality = os.path.join(directory, municipality)

            parser.add_folder(dir_municipality)

    # Decide between all together and

    # Also summarize the data:
    # Language pairs

    # Export data PER country as TMX. Includes some metadata? Make sure to be valid tmx1.4

    return


if __name__ == '__main__':
    DIRECTORY = r"C:\Users\Laurens\Data\C4C\translations\trafilatura_temp\trafilatura"

    main(directory=DIRECTORY)
