# The Containers and Repositories of Dr. Moreau

The purpose of this project is to: randomly create 20 bizzare animals and print one of them and
                                 : breed 2 randomly selected animals and print the new animal, with its parents

## Installation

Install this project by cloning the repository, making the scripts executable, and adding them to your PATH. Follow:
```
git clone https://github.com/Aanchalaanchal/COE332.git
cd COE332
cd homework02
chmod +rx generate_animals.py
chmod +rx read_animals.py
chmod +rx test_read_animals.py
export PATH=/code:$PATH
```
or pull a copy of the container with
```
docker pull aanchalaanchal/json-breeder:1.0
```

## Running the code

To generate the animals do:
```
python3 generate_animals.py
```
To print a randomly chosen animal and breed 2 randomly chosen animals (and print the parents and the new animal):
```
python3 read_animals.py
```
##Docker Image

You can build a Docker image using the provided Dockerfile. Use the commands:
```
docker build -t <dockerhubusername>/json-breeder:1.0 .
```
An example of running the scripts inside a container is:
```
docker run --rm -it <dockerhubusername>/json-breeder:1.0 /bin/bash
generate_animals.py
read_animals.py sys.argv[1]
test_read_animals.py
```
## Test
Test testing if the program takes integers or a bool as animals to breed by running:
```
docker run --rm -it username/json-parser:1.0 /bin/bash
cd /home
generate_animals.py test.json
read_animals.py test.json
test_read_animals.py
```
