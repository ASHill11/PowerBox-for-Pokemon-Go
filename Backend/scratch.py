
class Pokemon:
    # Required Attributes
    def __init__(self, name, cp):
        self.name = name
        self.cp = cp

    

    attack = None
    health = None
    defense = None


x = Pokemon(input('Enter name: '), input('Enter CP: '))

print(x.name)


