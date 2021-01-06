from flask import Flask
from flask_restful import Api
from resources.trainModel import TrainModel
from resources.routeTest import routeTest
from flask_cors import CORS
import config.configDb

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(TrainModel, '/trainModel', '/trainModel/<string:id>')
api.add_resource(routeTest, '/routeTest', '/routeTest/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
