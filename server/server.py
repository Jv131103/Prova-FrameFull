from flask import Flask
from main import blueprint
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api/produtos": {"origins": "http://localhost:3000"}})
CORS(app, resources={r"/api/users": {"origins": "http://localhost:3000"}})
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)