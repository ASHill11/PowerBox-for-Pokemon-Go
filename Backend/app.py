

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import sys


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return('Howdy')

# GPT
# Sample data to filter
pokedex = pd.read_csv("C:/Users/ashill11/Documents/VSCode Projects/PowerBox-for-Pokemon-Go/Data/Pokedex.csv")
pokedex_dict = {}
names = [i for i in pokedex.get('Name')]
numbers = [n for n in pokedex.get('No')]

counter  = 0
while counter < len(pokedex):
    pokedex_dict[numbers[counter], names[counter]] = names[counter]
    counter += 1


@app.route('/api/filter', methods=['POST'])
def filter_items():
    data = request.json
    if 'filter_value' in data:
        filter_value = data['filter_value'].lower()
        filtered_names = [item for item in names if filter_value in item.lower()]

        return jsonify({'items': filtered_items}), 200
    return jsonify({'error': 'Filter value not provided'}), 400

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