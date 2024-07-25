

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return('Howdy')

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
    app.run(host="0.0.0.0", port=4000)