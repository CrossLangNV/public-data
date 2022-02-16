from translate.storage.tmx import tmxfile

KEY_LANG = '{http://www.w3.org/XML/1998/namespace}lang'


def main(filename):
    with open(filename, 'rb') as f:
        tmx_file = tmxfile(f)

    n_units = len([_ for _ in tmx_file.unit_iter()])

    print(f"{filename}\nNumber of TU's: {n_units}")

    s_lang_sources = set()
    s_lang_targets = set()

    for tu in tmx_file.unit_iter():
        lang_source = tu.get_source_dom().get(KEY_LANG)
        lang_target = tu.get_target_dom().get(KEY_LANG)

        s_lang_sources.add(lang_source)
        s_lang_targets.add(lang_target)

    print(f"source languages:", *s_lang_sources)
    print(f"target languages:", *s_lang_targets)

    return


if __name__ == '__main__':
    # filename = r"C:\Users\Laurens\Data\C4C\translations\Italy.tmx"
    # filename = r"C:\Users\Laurens\Data\C4C\translations\Belgium.tmx"
    # filename = r"C:\Users\Laurens\Data\C4C\translations\Croatia.tmx"
    # filename = r"C:\Users\Laurens\Data\C4C\translations\Germany.tmx"
    # filename = r"C:\Users\Laurens\Data\C4C\translations\Norway.tmx"
    filename = r"C:\Users\Laurens\Data\C4C\translations\Slovenia.tmx"

    main(filename)
