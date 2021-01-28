from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import config.configDb

from resources.trainModel import TrainModel
from resources.user import User, Users
from resources.teacher import Teacher, Teachers

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(TrainModel, '/trainModel', '/trainModel/<string:id>')
api.add_resource(User, '/user', '/user/<string:email>/<string:password>')
api.add_resource(Users, '/users', '/users/<string:id>')
api.add_resource(Teacher, '/teacher', '/teacher/<string:email>/<string:password>')
api.add_resource(Teachers, '/teachers', '/teachers/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
