def my_sort():
    d = {
        "Hendrix": "1942",
        "Allman": "1946",
        "King": "1925",
        "Clapton": "1945",
        "Johnson": "1911",
        "Berry": "1926",
        "Vaughan": "1954",
        "Cooder": "1947",
        "Page": "1944",
        "Richards": "1943",
        "Hammett": "1962",
        "Cobain": "1947",
        "Garcia": "1942",
        "Beck": "1944",
        "Santana": "1947",
        "Ramone": "1948",
        "White": "1975",
        "Frusciante": "1970",
        "Thompson": "1949",
        "Burton": "1939",
    }

    sorted_set_years = sorted(set([int(year) for year in d.values()]))

    for year in sorted_set_years:
        names = []
        for name, year2 in d.items():
            if year == int(year2):
                names.append(name)
        sorted_names = sorted(names)
        for name in sorted_names:
            print(name)


if __name__ == "__main__":
    my_sort()
