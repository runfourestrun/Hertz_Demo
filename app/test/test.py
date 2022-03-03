import unittest
import pandas as pd
import random
from collections import Counter



def get_fields():

    df = pd.read_csv('/Users/alexanderfournier/PycharmProjects/Hertz/import/Car_Model_List.csv')
    category = df['Category']
    categories = [i.split(',') for i in category]
    result = {x for l in categories for x in l}
    for i in result:
        i.strip()

    for i in result:
        i.strip()
        print(f'"{i}"')


def car_category():
    car_categories = ["Convertible", "Sedan", " Pickup", "Van/Minivan", "SUV", " Wagon", "Coupe", "Hatchback"]
    weighted_probabilities = [.05, .35, .1, .01, .35, .05, .04, .05]
    choice = random.choices(car_categories,weighted_probabilities,k=1)
    selection = choice[0]
    return selection


_list = []
for i in range(100):
    test = car_category()
    _list.append(test)

print(Counter(_list))
