

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import sys


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return('Howdy')


# data to filter
pokedex = pd.read_csv("C:/Users/ashill11/Documents/VSCode Projects/PowerBox-for-Pokemon-Go/Data/Pokedex.csv")
pokedex_dict = {}

numbers = [n for n in pokedex.get('No')]
branch_codes = [nn for nn in pokedex.get('Branch_Code')]
names = [i for i in pokedex.get('Name')]

counter  = 0
while counter < len(pokedex):
    pokedex_dict[(numbers[counter], branch_codes[counter], names[counter])] = names[counter]
    counter += 1

# GPT
@app.route('/api/filter', methods=['POST'])
def filter_items():
    data = request.json
    if 'filter_value' in data:
        filter_value = data['filter_value'].lower()

        # Joke
        if not filter_value:
            # And much easier than dealing with an empty value, apparently
            filter_value = '201'
                                                                                                      
        # I don't want just a dash or underscore returning the whole list, so I'm hard-coding it to return nothing
        if filter_value == '-' or filter_value == '_':
            filtered_names = ['No results!']
            return jsonify({'items': filtered_names}), 200

        # While the user is typing they may pause on their last typed character
        # This modifies the string to chop off a trailing dash so as to not clear their filter
        if filter_value[-1] in ['-', '_']:
            filter_value = filter_value[:-1]

        # Permits the use of '-' in addition to '_' for the branch code
        if '-' in filter_value:
            filter_value = filter_value.replace('-', '_')


        # Filter the items
        filtered_items = [
            (branch_code, value) for (number, branch_code, key), value in pokedex_dict.items()
            if filter_value in key.lower() or filter_value == str(number) or filter_value == branch_code.lower()
        ]
        
        # Sort the filtered items by branch_code
        filtered_items.sort(key=lambda x: x[0])
        
        # Extract only the names for the response
        filtered_names = [value for branch_code, value in filtered_items]
        
        # Specific exclusions
        if filter_value == '1':
            filtered_names.remove('Zygarde 10% Form')  # Use discard if using a set
        if filter_value == '5':
            filtered_names.remove('Zygarde 50% Form')  # Use discard if using a set
        
        if len(filtered_names) == 0:
            filtered_names.append('No results!')
            
        return jsonify({'items': filtered_names}), 200
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