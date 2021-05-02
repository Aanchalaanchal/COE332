#!/usr/bin/env python3
import random
import json
import petname
import uuid
import datetime
import sys
import redis

rd = redis.StrictRedis(host='127.0.0.1', port=6408, db=0)

def redis_list(count, animal):
   rd.hmset(count,animal)

given_animals={"animals":[]}
given_list=['snake', 'bull', 'lion', 'raven', 'bunny']
for x in range(100):
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
                "tail": tails,
                "uid" : str(uuid.uuid4()),
                "created on" : str(datetime.datetime.now())}

   given_animals['animals'].append(new_animal)
   redis_list(x, animal)

   with open("animals.json", "w") as outfile:
       json.dump(given_animals, outfile)
