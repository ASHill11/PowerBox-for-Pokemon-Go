

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return('Howdy')

# GPT
@app.route('/api/input', methods=['POST'])
def process_input():
    data = request.json
    if 'input_value' in data:
        input_value = data['input_value']
        if isinstance(input_value, int):
            print(f'Input received! >{input_value}<')

            return jsonify({'message': f'Input value received: {input_value}'}), 200
        else:
            return jsonify({'error': 'Input value must be an integer'}), 400
    return jsonify({'error': 'Input value not provided'}), 400

"""
This will be the main Python file which interfaces with other Python files, as well as being a hub for APIs

TODO:
- Add Pokedex
    - Consider whether to tie candy to the Pokedex or some other store
    - Mega energy, as well
- Add other global resources, such as stardust
"""  


# APIs



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)