"""
Script that converts all the available data to tmx.

TODO
 -
"""
import os

from CEFAT4Cities.scripts.utils import Country, get_country


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


class Parser:
    def __init__(self, country):
        self.country = country

    def add_folder(self, dir: str):
        """

        :param dir: Path to directory with translation jsons.
        :return:
        """
        # TODO
        return


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
