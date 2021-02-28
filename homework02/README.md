# The Containers and Repositories of Dr. Moreau

The purpose of this project is to breed two randomly selected animals.

## Installation

Install this project by cloning the repository, making the scripts executable, and adding them to your PATH. For example:
```
git clone ??
chmod??
```
## Running the code

This code has ___ functions: function 1, function 2,
To do function 1:
```
blah
```
To do function 2:
```
blah
```
##Docker Image

You can build a Docker image using the provided Dockerfile. Use the commands:
```
git clone ...
cd repo/
docker build -t <dockerhubusername>/<code>:<version> .
```
An examples of running the scripts inside a container is:
```
docker run ....     # generate_animals.py
docker run ....     # read_animals.py
```
## Test
Test XYZ aspect of code by running:
```
docker run --rm -it username/json-parser:1.0 /bin/bash
cd /home
generate_animals.py test.json
read_animals.py test.json
```
