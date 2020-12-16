from flask import Flask
from flask_restful import Api
from endpoints.FakeReviewClassifier import FakeReviewClassifier
import logging
from flask_cors import CORS

logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

api = Api(app)

api.add_resource(FakeReviewClassifier, '/classify')

if __name__ == '__main__':
    app.run(debug=True,port=5000)
