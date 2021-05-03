#!/usr/bin/env python3
import json
from flask import Flask, request
import petname
import random
import uuid
import datetime
import redis

app = Flask(__name__)

@app.route('/create', methods=['GET'])
def create_database():
    rd = redis.StrictRedis(host='redis', port=6379, db=8)
    given_animals={"animals":[]}
    given_list=['snake', 'bull', 'lion', 'raven', 'bunny']
    for _ in range(100):
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
       rd.hmset(x, new_animal)
    return "database created"

def get_data():
    rd = redis.StrictRedis(host='redis', port=6379, db=8)
    userdata = {"animals":[]}
    for x in range(100):
        new_animal={"head": str(rd.hget(x, 'head')),
                     "body": str(rd.hget(x, 'body')),
                     "arms": str(rd.hget(x, 'arms')),
                     "legs": str(rd.hget(x, 'legs')),
                     "tail": str(rd.hget(x, 'tail')),
                     "uid" : str(rd.hget(x, 'uid')),
                     "created on" : str(rd.hget(x, 'creation time'))}
        userdata['animals'].append(animal)
    return userdata


@app.route('/animals', methods=['GET'])
def getanimals():
        new_output = [x for x in jsonList]
        return new_output
        print (new_output)

@app.route('/animals/heads/bunny', methods=['GET'])
def getheads():
        output2 = [x for x in jsonList if x['head'] == 'bunny']
        return output2
        print (output2)

@app.route('/animals/legs/6', methods=['GET'])
def getlegs():
        output3 = [x for x in jsonList if x['legs'] == 6]
        return output3
        print (output3)












@app.route('/animals/time', methods=['GET', 'POST'])
def time_query():
    if request.method == 'POST':
        start = request.form.get("name_start") + " 00:00:00.000000"
        end = request.form.get("name_end") + " 00:00:00.000000"
        print('animals created between {} and {} are '.format(start_date, end_date))
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S.%f')
        end = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S.%f')
        for x in data["animals"]:
            curr = datetime.datetime.strptime(x["created on"], '%Y-%m-%d %H:%M:%S.%f')
            if start < curr and curr < end:
                print(x)
                return x

@app.route('/animals/time/<start> <end>', methods=['GET', 'POST'])
def query_time(start, end):
    start += " 00:00:00.000000"
    end += " 00:00:00.000000"
    print('animals created between {} and {} are '.format(start_date, end_date))
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S.%f')
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S.%f')
    for x in userdata["animals"]:
        curr = datetime.datetime.strptime(x["created on"], '%Y-%m-%d %H:%M:%S.%f')
        if start < curr and curr < end:
            print(x)
            return x

@app.route('/animals/select/<uid>', methods=['GET'])
def select(uid):
    for x in userdata["animals"]:
        if x["uid"] == uid:
            print(x)
    return select(uid)
    print(select(uid))

@app.route('/animals/update/<uid>', methods=['GET', 'POST'])
def update(uid):
    if request.method == 'POST':
        head = request.form.get("head")
        body = request.form.get("body")
        arms = request.form.get("arms")
        legs = request.form.get("legs")
        tail = request.form.get("tail")
        for x in data["animals"]:
            if x['uid'] == uid:
                x["head"] = head
                x["body"] = body
                x["arms"] = arms
                x["legs"] = legs
                x["tail"] = tail
        with open('animals.json', 'w') as json_file:
            json.dump(userdata, json_file)
    return update(uid, head, body, arms, legs, tail)
    print(update(uid, head, body, arms, legs, tail))

@app.route('/animals/delete/<start> <end>', methods=['GET'])
def delete(start, end):
    start += " 00:00:00.000000"
    end += " 00:00:00.000000"
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S.%f')
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S.%f')
    userdata["animals"] = [element for element in userdata["animals"] if curr(element["created on"]) > end and curr(element["created on"]) < start]
    for i in range(len(userdata["animals"])):
        curr = datetime.datetime.strptime(userdata["animals"][i]["created on"], '%Y-%m-%d %H:%M:%S.%f')
        if start < curr and curr < end:
            print("to be deleted")
            print(userdata["animals"][i])
            userdata["animals"].pop(i)
    for x in userdata["animals"][:]:
        curr = datetime.datetime.strptime(x["created on"], '%Y-%m-%d %H:%M:%S.%f')
        print(x)
        if start < curr and curr < end:
            print("to be deleted")
            userdata["animals"][:].remove(x)
    print("updated deleted")
    print(userdata["animals"])
    with open('animals.json', 'w') as json_file:
        json.dump(userdata, json_file)
    return delete_by_date(start, end)
    print(delete_by_date(start, end))

@app.route('/animals/count/avg_legs', methods=['GET'])
def avg_legs():
    count = 0.0
    for x in userdata["animals"]:
        count += 1.0
    sum = 0
    for x in userdata["animals"]:
        sum += x["legs"]
    avg = sum/count()
    return avg
    print (avg)


@app.route('/animals/count/total', methods=['GET'])
def total():
    count = 0.0
    for x in userdata["animals"]:
        count += 1.0
    return count
    print (count)














if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
