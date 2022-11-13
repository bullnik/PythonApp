from flask import Flask
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)

class Result():
    def __init__(self, value: str, type: str):
        self.value = value
        self.type = type

    def to_dict(self):
        dict = {}
        dict['value'] = self.value
        dict['skilltype'] = self.type
        return dict

class Direction(Resource):
    def get(self, request: str):
        response = []
        response.append(Result(request, 'skill').to_dict())
        response.append(Result('jiba', 'knowledge').to_dict())
        response.append(Result('jiba3', 'skill').to_dict())
        response.append(Result('jiba4', 'knowledge').to_dict())
        response.append(Result('jiba5', 'knowledge').to_dict())

        return response, 200

class Requirements(Resource):
    def get(self, request: str):
        response = []
        response.append(Result(request, 'skill').to_dict())
        response.append(Result('jiba', 'knowledge').to_dict())
        response.append(Result('jiba3', 'skill').to_dict())
        response.append(Result('jiba4', 'knowledge').to_dict())
        response.append(Result('jiba5', 'knowledge').to_dict())
        response.append(Result(request, 'skill').to_dict())
        response.append(Result('jiba', 'knowledge').to_dict())
        response.append(Result('jiba3', 'skill').to_dict())
        response.append(Result('jiba4', 'knowledge').to_dict())
        response.append(Result('jiba5', 'knowledge').to_dict())

        return response, 200
    
api.add_resource(Direction, "/dir", "/dir/", "/dir/<string:request>")
api.add_resource(Requirements, "/req", "/req/", "/req/<string:request>")
if __name__ == '__main__':
    app.run(debug=True)