

class Pokemon:
    _instance_count_ = 0

    
    def __init__(self, number, name, cp, attack, defense, health):
        # Required Attributes

        # Generate a unique ID for each instance of this class, as you can have many of the same Pokemon.
        Pokemon._instance_count_ += 1
        self.id = Pokemon._instance_count_

        # sent over by the web UI
        self.number = number        # in Pokedex
        self.name = name
        self.cp = cp

        # You can derive many more attributes from these 
        self.attack = attack        # integer, 0-15
        self.defense = defense      # integer, 0-15
        self.health = health        # integer, 0-15
        # The search '(N)attack' will return Pokemon with the matching attack appraisal (int 0-4)
        # The search 'attack(N) will return Pokemon with the matching attack stat (int 0-15)

    
    # All other attributes
    # For now, just putting everything here that I can rembemeber. Functionality will be added later

    # Due to the game not not meaningfully differentiating between the HP IVs and HP (hit points), I have had to choose to call one 'HP' and the other 'health'
    # This is hit points
    nickname = None         # string: 'nickname'
    HP = None               # integer: X
    sex = None              # string: male, female, or None
    region = None           # string: <REGION>
    year = None             # integer: 20XX

    type1 = None            # string: <TYPE>
    type2 = None            # string: <TYPE> OR None

    fast_move = None        # string: 'name'
    charged_move1 = None    # string: 'name'
    charged_move2 = None    # string: 'name' OR None

    weight = None           # float: x.xx (kg)
    height = None           # float: x.xx (m)
    classification = None   # string: 'XXL', 'XL', 'XS', or 'XXS'

    tags = []   # Items in list defined by user, should all be stored as strings

    # NOTE: Currently no way of knowing these values without significant trial and error on the user's end in the first place.
    # Not to mention, that the program would need to age the Pokemon stored in it to maintain accuracy.
    age = None              # integer: N (days)
    # Distance is calculated from present location, meaning this may well be useless to add have.
    # For now, it is here as a placeholder to be sure I haven't missed anything.
    distance = None         # integer: N (km)


    # Binary attributes
    # 1 is yes, 0 is no
    _favorite_ = 0      # Favorited?
    _tagged_ = 0        # Tagged NOTE: In game search uses '#' for this filter

    _costume_ = 0       # Costume?
    _shiny_ = 0         # Shiny?

    _eggsonly_ = 0      # Egg-exclusive?
    _hatched_ = 0       # Hatched?

    _shadow_ = 0        # Shadow?
    _purified_ = 0      # Purified?

    _legendary_ = 0     # Legendary?
    _mythical_ = 0      # Mythical?
    _ultra_beasts_ = 0  # Ultra Beast?

    _traded_ = 0        # Traded?
    _lucky_ = 0         # Lucky?

    _item_ = 0          # Evolves with item?
    _tradeevolve_ = 0   # Evolves with trade?


    
x = Pokemon(input('Enter name: '), input('Enter CP: '))

print(x.name)


