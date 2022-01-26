"""
This script will do a couple of things:

 - Summary report of succeeded translations
 - Group correct files to be submitted at

"""

# Get all files

# Get the jsonl's

# Get the translations

# Check for empty inputs

# Check for failed outputs -> Save the outputs and group returned strings and count.
import json
import os
import re
import warnings
from enum import Enum
from typing import Union

# TODO add to arg or use default value.
# Directory with municipalities and then files.
# We expect we only need the json-l's and their translations.
DIRECTORY = r"C:\Users\Laurens\Data\C4C\translations\trafilatura_temp\trafilatura"
# DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)))

DIR_SAVE = os.path.join(DIRECTORY, 'export')


def make_dir(dirname):
    if not os.path.exists(dirname):
        print(f"Creating dir: {dirname}")
        os.makedirs(dirname)


make_dir(DIR_SAVE)

# Variable names
SUCCESS = 'success'
EXCEPT = 'exception'


def main(a=False):
    """
    User-script
    :return:
    """

    def generate_translated_jsonl_filenames(directory):
        """

        :param directory:
        :return: filenames to the JSON-L's
        """

        for municipality in os.listdir(directory):

            dir_municipality = os.path.join(directory, municipality)

            if not os.path.isdir(dir_municipality):
                continue

            # Check if
            for file in os.listdir(dir_municipality):
                # Filter on translated json-l
                if "translated" in file and ".jsonl" in file:
                    filename = os.path.join(dir_municipality, file)

                    yield filename

    def get_orig(file_or_filename):
        """
        First get everything before 'translated' and then before dot.
        :param file_or_filename:
        :return:
        """

        return file_or_filename.rsplit("translated", 1)[0].rsplit(".", 1)[0]

    d_content = {}

    d_select = {err.value: 0 for err in TranslationError}
    d_select[SUCCESS] = 0

    for filename in generate_translated_jsonl_filenames(DIRECTORY):
        filename_orig = get_orig(filename)

        if not os.path.exists(filename_orig):
            warnings.warn(f"Could not find file: {filename_orig}", UserWarning)

        data_trans = JSONL(filename)
        # json_l.export()

        for d in data_trans:

            if isinstance(d, TranslationError):
                d_select[d.value] += 1

            else:
                d_select[SUCCESS] += 1

                c = d["translated_content"]

                if a:
                    if c in d_content:
                        d_content[c] += 1
                    else:
                        d_content[c] = 1

        print(d_select)

        if a:
            l_sorted = [(k, v) for k, v in sorted(d_content.items(), key=lambda item: item[1], reverse=True)]

            print("Most common strings:")
            print(f"{l_sorted[0]}")
            print(f"{l_sorted[1]}")
            print(f"{l_sorted[2]}")

    return 0  # Success


class TranslationError(Enum):
    ISE = "Internal Server Error"
    TMR = "Too Many Requests"
    PE = "Parse Error"


class JSONL(list):
    """
    To parse the translated JSON-L's
    """

    def __init__(self, filename):
        # Opening JSON-Lines file
        with open(filename, 'r', encoding="utf-8") as json_file:
            json_list = json_file.read().splitlines()

        l = [self.parse_json(s_j) for s_j in json_list]

        # TODO implement here?
        # l = get_data(filename)
        super().__init__(l)

        self.l_str = json_list

    @staticmethod
    def parse_json(json_str,
                   debug=False) -> Union[dict, TranslationError]:

        KEY_ID = "id"
        KEY_title = "title"
        KEY_URL = "url"
        KEY_CONTENT = "translated_content"

        def clean_error(d):

            content = d.get(KEY_CONTENT)

            # Check for Translated content
            for err in TranslationError:
                if err.value == content:
                    return err

            return d

        # First try to use normal script.
        try:
            j = json.loads(json_str)
        except json.decoder.JSONDecodeError:
            # Let's try something else
            pass
        else:
            return clean_error(j)

        pattern = rf'^({{"{KEY_ID}"\s?:\s?")(.+)(",\s?"{KEY_title}":\s?")(.+)(",\s?"{KEY_URL}":")(.+)(",\s?"{KEY_CONTENT}":\s?")(.+)("}})'

        match = re.match(pattern, json_str)
        try:
            _, _id, _, _title, _, _url, _, _content, _ = match.groups()
        except:
            return TranslationError.PE

        d = {
            KEY_ID: _id,
            KEY_title: _title,
            KEY_URL: _url,
            KEY_CONTENT: _content,
        }

        r = Result(**d)

        return clean_error(d)

    def export(self):
        """
        Only save lines that are OK.

        :return:

        TODO
         - First we are just printing it.
        """

        l = []

        statistics = {e: 0 for e in TranslationError}
        statistics[SUCCESS] = 0

        for j, s in zip(self, self.l_str):
            if isinstance(j, TranslationError):
                # skip
                statistics[j] += 1
                continue

            else:
                statistics[SUCCESS] += 1

            # Write to file
            l.append(s)

        # TODO write to file instead of print.
        print(statistics)
        print(l)
        return l


class Result:
    def __init__(self, *args, translated_content=None, **kwargs):

        self.args = args
        self.kwargs = kwargs

        if translated_content is not None:

            if translated_content == TranslationError.ISE.value:
                self.translated_content = TranslationError.ISE
            elif translated_content == TranslationError.TMR.value:
                self.translated_content = TranslationError.TMR
            else:
                self.translated_content = translated_content


if __name__ == '__main__':
    # TODO convert to proper user script with args.
    main(a=False)
