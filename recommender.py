from flask import Flask, request, Response, json
import sys
from pathlib import Path

app = Flask(__name__)

status = {}

try:
    # load model here
    status["isready"] = True
    status["message"] = ""
except BaseException as error:
    status["isready"] = False
    status["message"] = "Error 3:"  + str(sys.exc_info()[0]) + str(error)

# define additional helper methods


# this method could be the main one that supplies the recommendation
@app.route("/recommendation", methods=['POST'])
def get_recommendation():
    try:
        if(status["isready"] == False):
            return Response(json.dumps({
            "code": 500,
            "name": 'Internal Server Error',
            "description": status["message"],
            }), status=500, mimetype='application/json')

        # gets the data that was sent in the request
        json_object = request.get_json()
    
        # do something with json_object - i.e. feed it to the model to get back some output

        result = [] # store a list of building objects here

        # simulate items resturned by model
        for i in range(0,1):
            output = {}
            output["building_id"] = 1000
            output["option_id"] = 2001
            output["latitude"] = 40.71455
            output["longitude"] = -74.00712
            output["predicted_roi"] = 0.1
            output["ranking"] = 1
        
            result.append(output)
            
        return json.dumps(result)

    except BaseException as error:
        return Response(json.dumps({
        "code": 500,
        "name": 'Internal Server Error',
        "description": "Error 3:"  + str(sys.exc_info()[0]) + str(error),
        }), status=500, mimetype='application/json')    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
