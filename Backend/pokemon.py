

class Pokemon:
    _instance_count_ = 0

    
    def __init__(self, name, cp, attack, defense, health):
        # Required Attributes

        # Generate a unique ID for each instance of this class, as you can have many of the same Pokemon.
        Pokemon._instance_count_ += 1
        self.id = Pokemon._instance_count_

        # sent over by the web UI
        self.name = name
        self.cp = cp

        # You can derive many more attributes from these 
        self.attack = attack        # Integer, 0-15
        self.defense = defense      # Integer, 0-15
        self.health = health        # Integer, 0-15
        # The search '(N)attack' will return Pokemon with the matching attack appraisal (int 0-4)
        # The search 'attack(N) will return Pokemon with the matching attack stat (int 0-15)

    
    # All other attributes
    # For now, just putting everything here that I can rembemeber. Functionality will be added later

    # Due to the game not not meaningfully differentiating between the HP IVs and HP (hit points), I have had to choose to call one 'HP' and the other 'health'
    # This is hit points
    HP = None

    type1 = None
    type2 = None

    fast_move = None
    charged_move1 = None
    charged_move2 = None

    sex = None

    weight = None
    height = None

    tags = []


    # Binary attributes
    # 1 is yes, 0 is no

    # Innate qualities
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


    
x = Pokemon(input('Enter name: '), input('Enter CP: '))

print(x.name)


