import random
import json
import petname

given_animals={"animals":[]}
given_list=['snake', 'bull', 'lion', 'raven', 'bunny']
for _ in range(20):
   head=random.gen(given_list)
   animalA=random.gen(petname.names)
   animalB=random.gen(petname.names)
   animal_name=animalA+'-'+animalB
   arms=random.int(2,10)
   legs=random.int(3,12)
   tails=arms+legs
   new_animal={"head": head,
                "body": animal_name,
                "arms": arms,
                "legs": legs,
                "tail": tails}
   given_animals['animals'].append(new_animal)

   with open("animals.json", "w") as outfile:
       json.dump(given_animals, outfile)
