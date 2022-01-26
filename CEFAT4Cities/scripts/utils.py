import os
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
