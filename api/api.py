from flask import Flask, jsonify, request
from flask_cors import CORS
import json



app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)



# API endpoints
@app.route('/post/bandById', methods=['POST'])
def post_specific_band_by_id():
    data = request.json
    # Process the data as needed
    print(data)
    # Send a response back to the Vue.js application
    response = {'message': 'Data received successfully'}
    return jsonify(response)

@app.route('/get/allBands', methods=['GET'])
def get_bands():
    with open("DataBase/bands.json") as json_file:
        data = json.load(json_file)
    return data


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)