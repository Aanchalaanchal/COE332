import json
from flask import Flask, request

app = Flask(__name__)

def get_data():
    with open("animals.json", "r") as json_file:
        userdata = json.load(json_file)
    return userdata
test = get_data()
print (type(test))
jsonList = test['animals']
print (type(jsonList))
output1 = [x for x in jsonList if x['head'] == 'snake']
print (output1)


@app.route('/animals')
def getanimals():
        new_output = [x for x in jsonList]
        return new_output
        print (new_output)

@app.route('/animals/heads/bunny')
def getheads():
        output2 = [x for x in jsonList if x['head'] == 'bunny']
        return output2
        print (output2)

@app.route('/animals/legs/6')
def getlegs():
        output3 = [x for x in jsonList if x['legs'] == 6]
        return output3
        print (output3)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
