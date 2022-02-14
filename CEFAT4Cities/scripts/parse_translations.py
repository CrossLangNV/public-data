"""
Script that converts all the available data to tmx.
"""
import glob
import os
import warnings
from typing import List, Optional

from pydantic import BaseModel, validator
from translate.storage.tmx import tmxfile

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
    url: str
    lang_source: str
    lang_target: str

    @validator('lang_source', "lang_target")
    def lower_case(cls, v):
        return v.lower()


class Parser:
    def __init__(self, country):
        self.country = country  # TODO use.

        self.summaries: List[Summary] = []

    def add_folder(self, directory: str):
        """

        :param dir: Path to directory with translation jsons.
        :return:
        """

        # TODO

        def get_target_lang(filename_json):
            """

            :param filename_json:
            :return:
            """

            _, s_trans_lang, s_json = filename_json.rsplit('.', 2)

            lang = s_trans_lang.rsplit("_", 1)[-1]

            if lang != "en":
                warnings.warn(f"Expected all this data to be translated to English: lang = {lang}", UserWarning)

            return "en"

        def get_content(page_trans: PageTrans):
            # page_orig = match_page_orig(data_orig, page_trans.id)
            # page_orig.content_html

            data = get_text_source(page_trans)

            content = clean_newlines(data)
            return content

        def get_text_source(page_trans: PageTrans,
                            source_lang='nl'):
            # Get from f"{id}_{lang_code}.txt."

            fn_txt_orig = directory + f"/{page_trans.id}_{source_lang}.txt"
            if not os.path.exists(fn_txt_orig):
                # Find te path
                endPaths = glob.glob(directory + f"/{page_trans.id}_??.txt")
                if len(endPaths) != 1:
                    warnings.warn(f"Expected only 1 match: {endPaths}")

                fn_txt_orig = endPaths[0]
            with open(fn_txt_orig, 'r', encoding="utf8") as file:
                data = file.read()
            return data

        def match_page_orig(data_orig, id) -> PageOrig:
            """

            :param data_orig:
            :param id: from page trans
            :return:
            """
            for d_orig in data_orig:
                if d_orig["id"] == id:
                    return PageOrig(**d_orig)

        # Go over translated jsons.
        for name_translated_json in filter(filter_translated_json, os.listdir(directory)):
            filename_translated_json = os.path.join(directory, name_translated_json)

            filename_orig = get_orig(filename_translated_json)

            lang_target = get_target_lang(filename_translated_json)

            if not os.path.exists(filename_orig):
                warnings.warn(f"Could not find file: {filename_orig}", UserWarning)

            data_trans = JSONL(filename_translated_json)

            data_orig = JSONL(filename_orig)

            for d in data_trans:
                if isinstance(d, TranslationError):
                    continue

                try:
                    page_trans = PageTrans(**d)

                    page_orig = match_page_orig(data_orig, page_trans.id)

                    summary = Summary(content=get_content(page_trans),  # TODO retrieve original content
                                      translated_content=clean_newlines(page_trans.translated_content),
                                      url=page_orig.url,
                                      lang_source=page_orig.language,
                                      lang_target=lang_target)

                except:
                    print(f"!Failed to generate summary of {d.get('id')}")
                else:
                    self.summaries.append(summary)

    def export(self, filename: str, debug=False):
        """
        Create a TMX from the summaries
        :return:
        """

        tmx_file = tmxfile(
            sourcelanguage=self.estimate_source_lang(),  # TODO add possible information
            targetlanguage=self.estimate_target_lang()
        )

        for summ in self.summaries:
            tmx_file.addtranslation(source=summ.content,
                                    srclang=summ.lang_source,
                                    translation=summ.translated_content,
                                    translang=summ.lang_target,
                                    comment=summ.url  # TODO city/website info
                                    )

        # Debug:
        if debug:
            for node in tmx_file.unit_iter():
                print(node.source, node.target)

        tmx_file.savefile(filename)

        return

    def estimate_source_lang(self):
        """
        estimates the source language

        :return:
        """

        return self.summaries[0].lang_source

    def estimate_target_lang(self):
        """
        estimates the source language

        :return:
        """

        return self.summaries[0].lang_target


def main(directory, i_start: int = 0):
    for i, country in enumerate(Country):
        if i < i_start:
            continue

        print(f"Country {i + 1}/{len(Country)}")

        parser = Parser(country=country.value)

        l_mun = list(get_municipalities_by_country(directory, country))
        for j, municipality in enumerate(l_mun):
            print(f"Municipality {j + 1}/{len(l_mun)}")

            dir_municipality = os.path.join(directory, municipality)

            parser.add_folder(dir_municipality)

        parser.export(country.value + '.tmx')

    # Decide between all together and

    # Also summarize the data:
    # Language pairs

    # Export data PER country as TMX. Includes some metadata? Make sure to be valid tmx1.4

    return


if __name__ == '__main__':
    # DIRECTORY = r"C:\Users\Laurens\Data\C4C\translations\trafilatura_temp\trafilatura"
    DIRECTORY = os.path.abspath(os.path.dirname(__file__))

    main(directory=DIRECTORY, i_start=2)
