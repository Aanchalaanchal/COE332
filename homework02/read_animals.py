#!/usr/bin/env python3
import json
import random
import sys

def main():

    with open(sys.argv[1], 'r') as f:
        animal_dict = json.load(f)

    print(random.choice(animal_dict['animals']))

    parent1 = random.choice(animal_dict['animals'])
    parent2 = random.choice(animal_dict['animals'])
    head = random.choice(parent1['head'] + parent2['head'])
    animal_name = random.choice(parent1['body'] + parent2['body'])
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

if __name__ == '__main__':
    main()
