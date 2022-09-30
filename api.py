from flask import Flask, jsonify
from flask_restful import Resource, reqparse, Api
import controller
import json


app = Flask(__name__)
api = Api(app)

res = {
    'resident1': 'Jerry',
    'resident2': 'Sam',
    'resident3': 'Will',
}




parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('age')

class Residents(Resource):

    def get(self, residentId = None):
        if residentId == None:
            ret = controller.getResidents()
        else:
            ret = controller.getResidentsById(residentId)
        return jsonify(ret)

    def put(self, residentId):
        args = parser.parse_args()
        name = args['name']
        age = args['age']
        ret = controller.updateResidentById(residentId,name, age)
        return jsonify(ret)

    def post(self):
        args = parser.parse_args()
        name = args['name']
        age = args['age']
        ret = controller.insertResident(name, age)
        return jsonify(ret)

    
    def delete(self, residentId):
        ret = controller.deleteResidentsById(residentId)
        return jsonify(ret)

api.add_resource(Residents,'/residents/<residentId>', '/residents')

if __name__ == '__main__':
    app.run(debug=True)