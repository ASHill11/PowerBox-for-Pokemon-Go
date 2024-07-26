

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

numbers = [n for n in pokedex.get('No')]
branch_codes = [nn for nn in pokedex.get('Branch_Code')]
names = [i for i in pokedex.get('Name')]

counter  = 0
while counter < len(pokedex):
    pokedex_dict[(numbers[counter], branch_codes[counter], names[counter])] = names[counter]
    counter += 1


@app.route('/api/filter', methods=['POST'])
def filter_items():
    data = request.json
    if 'filter_value' in data:
        filter_value = data['filter_value'].lower()
        filtered_items = {
            value for (number, key), value in pokedex_dict.items()
            if filter_value in key.lower() or filter_value == str(number)
        }
        if filter_value == '1': filtered_items.remove(r'Zygarde 10% Form')
        if filter_value == '5': filtered_items.remove(r'Zygarde 50% Form')
        return jsonify({'items': list(filtered_items)}), 200
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