#!/usr/bin/env python3
import json
import random
import sys

def breed(parent1, parent2):
    head = parent1['head']
    animal_name = parent2['body']
    arms = parent1['arms']
    legs = parent2['legs']
    tails = parent1['tail']
    new_animal = {"head": head,
                  "body": animal_name,
                  "arms": arms,
                  "legs": legs,
                  "tail": tails}

    print("The new animal is", new_animal)
    print("The parents are: ", parent1, "and ", parent2)

def main():

    with open(sys.argv[1], 'r') as f:
        animal_dict = json.load(f)

    print(random.choice(animal_dict['animals']))

    a = random.choice(animal_dict['animals'])
    b = random.choice(animal_dict['animals'])

    breed(a, b)

if __name__ == '__main__':
    main()
