# I know, and I'm sure it's not the first time you've tried to understand "OOP" (object-oriented programming),
# is it? # Well here we go once again, but I'm sure Python will make things more pleasant. Let's start with a key
# concept, and that is "abstraction". Let's try something easy to not vary

# But tell me brainy what the heck is a Class, a class definition could be the generalization of any object,
# in other words to break down an object to identify its characteristics and behavior. But tell me brainy what the
# hell is a Class, a class definition could be the generalization of any object, in other words to break down an
# object to identify its characteristics and behavior. Ok, let's define our first class, how about starting with a
# glorious tangerine?

class Tangerine:

    def __init__(self, weight=20, size="small"):
        self.weight = weight
        self.size = size.lower()
        self.color = "Green"

    def set_maturity_degree(self, mature_state=False):
        if mature_state:
            self.color = "Orange"

    def is_ripe(self):
        if self.color == "Orange":
            print("Is ripe, yummy")
            return True
        else:
            print("Unripe, sorry")
            return False


# I know, a lot of gibberish.

mandarina = Tangerine(50, "Big")
otra_mandarina = Tangerine()

otra_mandarina.set_maturity_degree(True)

mandarina.is_ripe()
print(mandarina.weight)
otra_mandarina.is_ripe()
