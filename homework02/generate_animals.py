#!/usr/bin/env python3
import random
import json
import petname
import sys

def main():

        given_animals = {"animals":[]}
        given_list = ['snake', 'bull', 'lion', 'raven', 'bunny']

        for _ in range(20):
                head=random.choice(given_list)
                animalA=random.choice(petname.names)
                animalB=random.choice(petname.names)
                animal_name=animalA+'-'+animalB
                arms=random.randrange(2,11,2)
                legs=random.randrange(3,13,3)
                tails=arms+legs
                new_animal={"head": head,
                        "body": animal_name,
                        "arms": arms,
                        "legs": legs,
                        "tail": tails}
                given_animals['animals'].append(new_animal)

        with open("sys.argv[1]", "w") as outfile:
                json.dump(given_animals, outfile)

if __name__=='__main__':
        main()
