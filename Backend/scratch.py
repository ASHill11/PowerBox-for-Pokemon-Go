

class Pokemon:
    _instance_count_ = 0

    
    def __init__(self, name, cp):
        # Required Attributes

        # Generate a unique ID for each instance of this class, as you can have many of the same Pokemon.
        Pokemon._instance_count_ += 1
        self.id = Pokemon._instance_count_
        # sent over by the web UI
        self.name = name
        self.cp = cp

    

    _attack_ = None
    _health_ = None
    _defense_ = None


x = Pokemon(input('Enter name: '), input('Enter CP: '))

print(x.name)


