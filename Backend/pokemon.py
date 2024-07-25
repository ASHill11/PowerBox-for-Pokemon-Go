

import pandas as pd


pokedex_csv = pd.read_csv(r"C:\Users\ashill11\Documents\VSCode Projects\PowerBox-for-Pokemon-Go\Data\Pokedex.csv")

numbers = pokedex_csv.get('No')
branch_codes = pokedex_csv.get('Branch_Code')
names = pokedex_csv.get('Name')

for number, branch_code, name, in numbers, branch_codes, names:
    pass


class Pokemon:
    _instance_count_ = 0

    
    def __init__(self, name):
        # Init takes the bare minimum required attributes to build a Pokemon
        # Inputs should come from the client UI using POST

        # Generate a unique ID for each instance of this class, as you can have many of the same Pokemon.
        Pokemon._instance_count_ += 1
        self.id = Pokemon._instance_count_

        self.name = name

        # Pokedex numbers
        #number = 
        #branch_code = 

    cp = None               # integer: N   

    # You can derive many more attributes from these 
    attack = None           # integer: range(0-15)
    defense = None          # integer: range(0-15)
    health = None           # integer: range(0-15)
    # The search '(N)attack' will return Pokemon with the matching attack appraisal (int 0-4)
    # The search 'attack(N) will return Pokemon with the matching attack stat (int 0-15)

    
    # All other attributes
    # For now, just putting everything here that I can rembemeber. Functionality will be added later

    # Due to the game not not meaningfully differentiating between the HP IVs and HP (hit points), I have had to choose to call one 'HP' and the other 'health'
    # This is hit points
    hit_points = None       # integer: N
    nickname = None         # string: 'nickname'
    sex = None              # string: male, female, or None
    region = None           # string: <REGION>
    year = None             # integer: 20XX
    date = None             # string: mm/dd/yyyy # Format could be picked by user

    buddy = None            # integer: range(0-5)
    mega = None             # integer: range(1-3)

    type1 = None            # string: 'TYPE'
    type2 = None            # string: 'TYPE' OR None

    fast_move = None        # string: 'name'
    charged_move1 = None    # string: 'name'
    charged_move2 = None    # string: 'name' OR None

    weight = None           # float: x.xx (kg)
    height = None           # float: x.xx (m)
    size = None   # string: 'XXL', 'XL', 'XS', 'XXS, or None'
    # Also see: biggest / smallest, heaviest / lightest below

    # NOTE: Currently no way of knowing these values without significant trial and error on the user's end in the first place.
    # Not to mention, that the program would need to age the Pokemon stored in it to maintain accuracy.
    age = None              # integer: N (days)

    # Distance is calculated from present location, meaning this may well be useless to add have.
    # For now, it is here as a placeholder to be sure I haven't missed anything.
    distance = None         # integer: N (km)
    location = None         # string: 'placename'
    remote_location = None  # string: 'remoteplacename'
    event = None            # string: 'eventname'
    party_members = None    # list (of strings): ['trainername'] where len(party_members) <= 3


    # USER defined attributes
    tags = []   # Items in list defined by user, should all be stored as strings
    # NOTE: Probably will add the ability for users to create custom attributes 


    # Binary attributes
    # 1 is yes, 0 is no
    favorite = 0      # Favorited?
    tagged = 0        # Tagged NOTE: In game search uses '#' for this filter

    costume = 0       # Costume?
    shiny = 0         # Shiny?

    eggsonly = 0      # Egg-exclusive?
    hatched = 0       # Hatched?

    shadow = 0        # Shadow?
    purified = 0      # Purified?

    legendary = 0     # Legendary?
    mythical = 0      # Mythical?
    ultra_beasts = 0  # Ultra Beast?

    traded = 0        # Traded?
    lucky = 0         # Lucky?
    party = 0         # Caught in a party?
    raid = 0          # Caught in a raid?

    item = 0          # Evolves with item?
    tradeevolve = 0   # Evolves with trade?


    
x = Pokemon(input('Enter name: '), input('Enter CP: '))

print(x.name)


