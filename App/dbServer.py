from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import dbHandler

app = Flask(__name__)
CORS(app)

@app.route("/")
def pyConnTest():    
    print('API')
    return "Test API Success"

@app.route("/API" , methods=['POST'])
def Create():    
    print('Create API')

    json = request.get_json()
    print(json["ID"])
    print(json["NAME"])

    dbHandler.Create(json["ID"] , json["NAME"])
    return 'Sccess Create'

@app.route("/API")
def Read():    
    print('Read API')

    jsonData = dbHandler.Read()
    print('Sccess Read')
    print(jsonData)
    return jsonData

@app.route("/API" , methods=['PUT'])
def Update():    
    print('Update API')

    json = request.get_json()
    print(json["ID"])
    print(json["NAME"])

    dbHandler.Update(json["ID"] , json["NAME"])
    return 'Sccess Update'

@app.route("/API" , methods=['DELETE'])
def Delete():    
    print('Delete API')

    json = request.get_json()
    print(json["ID"])

    dbHandler.Delete(json["ID"])
    return 'Sccess Delete'
    
if __name__ == "__main__":
    print('Server Start')
    app.run()