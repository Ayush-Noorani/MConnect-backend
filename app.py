from flask import Flask, request, jsonify
from waitress import serve
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
users = [
    {'id': 1, 'name': 'Ayush', 'bio': 'Bio of Ayush'},
]

@app.route('/login', methods=['POST'])
def home():
    data = request.get_json()
    print("DATA : ", data)
    if data:
        return jsonify({"message": "Got the data",
                        "status": 200})
    return jsonify({"message": "Failed"})

@app.route('/getMentors', methods=['GET'])
def getMentors():
    return jsonify({"status": 200,
                    "data": [
                        {
                            "Name": "Ayush Noorani",
                            "Designation": "Software Developer",
                            "Company": "Oqton",
                            "Description": ""
                        },
                        {
                            "Name": "Rajeev Dessai",
                            "Designation": "Software Developer",
                            "Company": "Oqton",
                            "Description": ""
                        },
                        {
                            "Name": "Rohan Almeida",
                            "Designation": "Software Development Consultant",
                            "Company": "Oqton",
                            "Description": ""
                        },
                        {
                            "Name": "Omkar Naik",
                            "Designation": "Software Development Intern",
                            "Company": "Creative Capsule",
                            "Description": ""
                        }
                    ]})

@app.route('/getMentor/<name>', methods=['GET'])
def getSpecificMentor(name):
    user = next((user for user in users if user['name'] == name), None)
    if user:
        return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    # Run the app using Waitress
    serve(app, host='0.0.0.0', port=8080)
