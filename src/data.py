from numpy.lib.function_base import append
import pandas as pd
import pycountry

"""
Currently, this code is supposed to take
the data from species and fish_catches and
cleans it up so that it can be fed into the
neural network.
[0,1,3,4,5,6,7,8,9,10,11,12]:
[Species, area, Country, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006]
"""


def if_None(x):
    if x == "nan":
        return None
    return x

def save_data():
    all_species = pd.read_csv("data/species.txt", sep="\t", error_bad_lines=False, encoding='latin-1')
    fish_catches = pd.read_csv("data/fish_catches.csv")
    all_fish, all_areas = [], []

    for area in all_species["3A_CODE"]:
        area = f"{area}"
        if area not in all_areas:
            all_areas.append(if_None(area))

    for fish in fish_catches["Area"]:
        fish = f"{fish}"
        if fish not in all_fish:
            all_fish.append(if_None(fish))

    with open("data/fishing_areas.txt", "w+") as file:
        file.write(f"{all_areas}\n{all_fish}")

def get_data():
    content = 0
    with open("data/fishing_areas.txt", "r") as file:
        content = file.read()
    organized_content = content.split("\n")
    return eval(organized_content[0]), eval(organized_content[1])

def read_data():
    fish_catches = pd.read_csv("data/fish_catches.csv")
    fishing_species, fishing_areas = get_data()
    tableHeaders = [1,3,4,5,6,7,8,9,10,11,12]
    finalData = []

    for ind_data in fish_catches.iterrows():
        y = fishing_species.index(if_None(f"{ind_data[1][0]}"))
        x = []
        for header in tableHeaders:
            value = ind_data[1][header]
            if header == 1:
                try:
                    value = fishing_areas.index(if_None(f"{value}"))
                except ValueError:
                    value = None
            elif header == 3:
                try:
                    value = int(pycountry.countries.get(alpha_2=value).numeric)
                except:
                    value = None
            x.append(value)
        finalData.append([x, y])

    return finalData


