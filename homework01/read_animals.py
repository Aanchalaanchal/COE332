import json
import random

with open('animals.json') as openfile:
    generated_animals=json.load(openfile)
    print(generated_animals['animals'][random.randint(0,19)])
