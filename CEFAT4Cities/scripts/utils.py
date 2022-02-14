import os
import re
from enum import Enum


class Country(Enum):
    Croatia = "Croatia"
    Germany = "Germany"
    Belgium = "Belgium"
    Norway = "Norway"
    Slovenia = "Slovenia"
    Italy = "Italy"


def get_municipality(filename):
    dir_municipality, _ = os.path.split(filename)
    _, municipality = os.path.split(dir_municipality)

    return municipality


def get_country(municipality) -> Country:
    *_, country_code = municipality.split('.')

    if country_code == "hr":  # Croatia
        return Country.Croatia
    elif country_code == "de":
        return Country.Germany
    elif country_code == "be":
        return Country.Belgium
    elif country_code == "no":
        return Country.Norway
    elif country_code == "si":
        return Country.Slovenia
    elif country_code == "it":
        return Country.Italy
    # Exepctions:
    elif municipality == 'gerolstein.org':
        return Country.Germany
    elif municipality in ["halen", "hasselt", "koekelare", "houthalen-helchteren", "heusden-zolder", "herent",
                          "www.antoing.net"]:
        return Country.Belgium
    # elif municipality in []

    return


def clean_newlines(s):
    """
    The data did contain some newline errors.
    :param s:
    :return:

    TODO improve speed.
    """

    def single_regex(s):
        # single Regex.
        regex = r"((\\[nNrR])|[\n\r])+"
        repl = "\n"
        s_new = re.sub(regex, repl, s)
        s_new = s_new.strip(repl)  # Remove newlines from start and end.

        return s_new

    def split_regex(s):
        # single Regex.
        # regex = r"(\\[nNrR])+"
        regex = r"\\[nNrR]"
        repl = "\n"
        s_typo_corr = re.sub(regex, repl, s)

        s_clean = '\n'.join(filter(lambda x: x, map(str.strip, s_typo_corr.splitlines())))

        return s_clean

        # s_clean = '\n'.join(filter(lambda x: x.strip(), s_typo_corr.splitlines()))
        #
        #
        # s_new = s_new.strip(repl)  # Remove newlines from start and end.
        #
        # return s_new

    def old_multireplace(s):
        s_clean = s.replace('\\r', '\r').replace('\\R', '\r')
        s_clean = s_clean.replace('\\n', '\n').replace('\\N', '\n')
        # Remove empty lines.
        s_clean = '\n'.join(filter(lambda x: x.replace(' ', ''), s_clean.splitlines()))

        return s_clean

    if 1:
        return split_regex(s)
    elif 1:
        return single_regex(s)
    else:
        return old_multireplace(s)

    regex = r"(\\r)"
    regex = r"((\\){1,2}[rn])+"
    s_new = re.sub(regex, "\t", s)
    print(s_new)

    s.splitlines()

    pattern = "(\\\\[rR])|(\n)|(\r)|(\\\\r)"
    pattern = "((\\)?((\\)[rR])?(\\)?\\[nN])"
    # pattern = r"((\)?((\)[rR])?(\)?\[nN])"
    pattern = "(((\\)|)\\r(\\n)?)"
    # pattern = r"\(((\\)|)\\r(\\n)?\)"
    pattern = "((\\)|)\\r(\\n)?"

    regex = r"(<br/>)|(<EOF>)|(<SOF>)|[\n\!\@\#\$\%\^\&\*\(\)\[\]\
           {\}\;\:\,\.\/\?\|\`\_\\+\\\=\~\-\<\>]"

    regex = r"(<br/>)|(<EOF>)|(<SOF>)|[\n]"
    l = re.split(regex, s)

    re.split(regex, s)

    r"((\\r)\n)"

    pattern = r"\\r"

    pattern = r"(\\r)?\n"
    # pattern = r"(\\r)?\n"
    y = re.split(pattern, s)
    print(y)

    re.sub(pattern, "\t", s)

    # l =re.split(pattern, s)
    x = re.sub(pattern, '\n', s)
    print(x)

    # l = re.split(pattern, s)

    re.search(pattern, s, re.M)

    re.sub(pattern, '\n', s)

    # re.sub(pattern, s, "\n")

    l = re.split(pattern, s)

    s_clean = s.replace('\\r', '\r').replace('\\R', '\r')
    s_clean = s_clean.replace('\\n', '\n').replace('\\N', '\n')
    # Remove empty lines.
    s_clean = '\n'.join(filter(lambda x: x.replace(' ', ''), s_clean.splitlines()))
    return s_clean
