import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the data from the JSON file
with open('q-vercel-python.json', 'r') as f:
    data = json.load(f)

# Create a dictionary for quick lookup of marks by name
marks_dict = {entry['name']: entry['marks'] for entry in data}

@app.route('/api', methods=['GET'])
def get_marks():
    # Get the names from the query parameters
    names = request.args.getlist('name')
    
    # Look up the marks for each name
    marks = [marks_dict.get(name, None) for name in names]
    
    # Return the result in the specified JSON format
    response = {"marks": marks}
    
    # Set CORS headers to allow GET requests from any origin
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Define the handler for the serverless function
def handler(event, context):
    with app.test_request_context(event['path'], method='GET', args=event['queryStringParameters']):
        return app.full_dispatch_request()

