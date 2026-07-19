# Constructor is a special method in Python classes that is automatically called when a new instance of the class is created. 
    # It is defined using the `__init__` method and is used to initialize the attributes of the class. 
    # The constructor can take parameters to set initial values for the object's attributes.
# Constructor are used to initialize the attributes of an object when it is created.
# __init__ Function or Initialize Function is called when the object is created and it is used as a Constructor.
    # It is a special method in Python classes that is automatically called when a new instance of the class is created. 
    # The `__init__` method can take parameters to set initial values for the object's attributes.
# Self Parameter - the self parameter in '__init__' is pertaining to itself the object that is being created.

# Example of Constructor
class Character:
    def __init__(self, name, hp, mp, atk, lvl):  # Constructor with parameters
        self.name = name  # Initialize the name attribute
        self.hp = hp      # Initialize the hp attribute
        self.mp = mp      # Initialize the mp attribute
        self.atk = atk    # Initialize the atk attribute
        self.lvl = lvl    # Initialize the lvl 
        print ("Character Created: " + self.name)  # Print a message when a character is created

charOne = Character("Arjay", 100, 50, 12, 1)  # Create an instance of Character with specific values
charTwo = Character("Thily", 120, 60, 15, 2)  # Create another instance of Character with different values
charThree = Character("Cyndi", 80, 40, 10, 1)   # Create a third instance of Character with different values