from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import dbHandler

app = Flask(__name__)
CORS(app)

@app.route("/")
def pyConnTest():    
    print('API')

    # jsonData = dbHandler.ReadData()
    # return jsonify({"ID":"Johnny"})
    return "Test API Success"

@app.route("/API" , methods=['POST'])
def Create():    
    print('Create API')

    json = request.get_json()
    print(json["ID"])
    print(json["NAME"])
    
    # jsonData = dbHandler.ReadData()
    # return jsonify({"ID":"Johnny"})
    return 'Sccess Create'

@app.route("/API")
def Read():    
    print('Read API')

    # jsonData = dbHandler.ReadData()
    # return jsonify({"ID":"Johnny"})
    return 'Sccess Read'

@app.route("/API" , methods=['PUT'])
def Update():    
    print('Update API')

    json = request.get_json()
    print(json["ID"])
    print(json["NAME"])

    # jsonData = dbHandler.ReadData()
    # return jsonify({"ID":"Johnny"})
    return 'Sccess Update'

@app.route("/API" , methods=['DELETE'])
def Delete():    
    print('Delete API')

    json = request.get_json()
    print(json["ID"])

    # jsonData = dbHandler.ReadData()
    # return jsonify({"ID":"Johnny"})
    return 'Sccess Delete'
    
if __name__ == "__main__":
    print('Server Start')
    app.run()