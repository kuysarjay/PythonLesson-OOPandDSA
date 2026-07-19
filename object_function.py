# Object Function - it is a function that is used to perform a specific task or action on an object. It can be used to manipulate the attributes of an object or to perform some action related to the object.
    # any function declare inside a class is called an object function. It is used to perform a specific task or action on an object.
    # It can be used to manipulate the attributes of an object or to perform some action related to the object. 
    
class Character:
    def __init__(self, name, hp, mp, atk, lvl):  # Constructor with parameters
        self.name = name  # Initialize the name attribute
        self.hp = hp      # Initialize the hp attribute
        self.mp = mp      # Initialize the mp attribute
        self.atk = atk    # Initialize the atk attribute
        self.lvl = lvl    # Initialize the lvl 
        print ("Character Created: " + self.name)  # Print a message when a character is created

    def attack(self):  # Object function to perform an attack action
        print(f"{self.name} attacks with {self.atk} damage!")  # Print attack message
    
    def level_up(self):  # Object function to level up the character
        self.lvl += 1  # Increase the level by 1
        print(f"{self.name} has leveled up to level {self.lvl}!")  # Print level up message
        
charOne = Character("Arjay", 100, 50, 12, 1)  # Create an instance of Character with specific values
charOne.attack()  # Call the attack function for charOne
charOne.level_up()  # Call the level_up function for charOne