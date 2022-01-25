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

# TODO add to arg or use default value.
# Directory with municipalities and then files.
# We expect we only need the json-l's and their translations.
import warnings
import re

DIRECTORY = r"C:\Users\Laurens\Data\C4C\translations\trafilatura_temp\trafilatura"


def main():
    """
    User-script
    :return:
    """

    def generate_translated_jsonl_filenames(directory):
        """

        :param directory:
        :return: filenames to the JSON-L's
        """

        for municipality in os.listdir(DIRECTORY):

            dir_municipality = os.path.join(DIRECTORY, municipality)

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



    for filename in generate_translated_jsonl_filenames(DIRECTORY):
        filename_orig = get_orig(filename)

        if not os.path.exists(filename_orig):
            warnings.warn(f"Could not find file: {filename_orig}", UserWarning)

        data_trans = get_data(filename)
        data_orig = get_data(filename_orig)

        filename, filename_orig

    return 0  # Success


def get_data(filename_json, debug=False):
    """
    Converts the JSON-Lines file to list of python dict.
    :param filename_json:
    :return:

    TODO
     - This still isn't entirely correct. The problem occurs with all the backslashes.
    Notes
     - There are also too many double backslashes in the original, translated files where there should be only one.
    """

    # Opening JSON file
    with open(filename_json, 'r', encoding="utf-8") as json_file:
        json_list = list(json_file)

    for json_str in json_list:

        if not json_str: # Skip empty lines/end
            continue

        # Try to fix if '"' in string, but not as delimter.

        # Drop first, drop last
        json_str_cut = json_str.split('"', 1)[1].rsplit('"', 1)[0]
        l_pairs = json_str_cut.split('", "')

        l_pairs2 = []
        for pair in l_pairs:
            key, value = pair.split('":"', 1)

            # This is the line that fixes the double quotes within double quotes.

            value2 = value.replace('"', "''")

            pair2 = f'"{key}": "{value2}"'
            l_pairs2.append(pair2)

        json_str2 = ', '.join(l_pairs2)
        json_str3 = f'{{{json_str2}}}'

        # if json_str3 is

        if debug:
            print(json_str3)

        class LazyDecoder(json.JSONDecoder):
            def decode(self, s, **kwargs):
                regex_replacements = [
                    (re.compile(r'([^\\])\\([^\\])'), r'\1\\\\\2'),
                    (re.compile(r',(\s*])'), r'\1'),
                ]
                for regex, replacement in regex_replacements:
                    s = regex.sub(replacement, s)
                return super().decode(s, **kwargs)

        # result = json.loads(json_str, cls=LazyDecoder)
        result = json.loads(json_str3, cls=LazyDecoder)

        yield result


if __name__ == '__main__':
    # TODO convert to proper user script with args.
    main()
