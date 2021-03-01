#!/usr/bin/env python3
import json
import random
import sys

def main():

    with open('sys.argv[1]', 'r') as openfile:
        generated_animals=json.load(openfile)
        
    print(generated_animals['animals'][random.randint(0,19)])
if __name__=='__main__':
    main()
