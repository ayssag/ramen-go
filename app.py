from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
from os import environ
import json

DB_URL = environ.get('DB_URL')
API_KEY = environ.get('API_KEY')
API_URL = environ.get('API_URL')

app =  Flask('Ramen Go!')
CORS(app)

def connect_db(url: str, dbName):
    try:
        client = MongoClient(url)
        db = client[dbName]
        
        return db
    except:
        print('No Connection.')

db = connect_db(url=DB_URL, dbName='ramengo')

@app.route("/broths", methods=['GET'])
@cross_origin()
def get_broths():
    try:
        brothList = []
        for broth in db.broth.find():
            del broth['_id']
            brothList.append(broth)
        
        return jsonify(brothList), 200
    except Exception as e:
        print(f'{e}: Fail to list broths.')

@app.route("/proteins", methods=['GET'])
@cross_origin()
def get_proteins():
    try:
        proteinList = []
        for protein in db.protein.find():
            del protein['_id']
            proteinList.append(protein)
        
        return jsonify(proteinList), 200
    except Exception as e:
        print(f'{e}: Fail to get proteins.')

@app.route("/order", methods=['POST'])
@cross_origin()
def make_order():
    try:
        rawData = request.data.decode('utf-8')
        data = json.loads(rawData)

        brothId = data.get('brothId')
        proteinId = data.get('proteinId')
        
        broth = db.broth.find_one({"id": brothId})
        protein = db.protein.find_one({"id": proteinId})
        
        brothName = broth['name']
        proteinName = protein['name']
        
        requestData = {
            "url": API_URL,
            "x-api-key": API_KEY
        }
        if not requestData['x-api-key']:
            return 'x-api-key header missing', 403
        
        getOrderId = requests.post(
            url=requestData['url'],
            headers={'x-api-key': requestData['x-api-key']}
        )   
        
        orderId = json.loads(getOrderId.content)
        order = {
            "id": orderId["orderId"],
            "description": f'{brothName} and {proteinName} Ramen',
            "image": f"https://tech.redventures.com.br/icons/ramen/ramen{proteinName}.png"
        }
        return jsonify(order), 200
    
    except Exception as e:
        return f'{e}: Can\'t make a post request.'

@app.route("/")
@cross_origin()
def home():
    return '<h1>Ramen Go!</h1>'
    
if __name__ == '__main__':
    app.run()
