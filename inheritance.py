# Inheritance allows a child class to inherit methods and attributes from a parent class,
    # promoting code reusability and organization. 
# In Python, inheritance is implemented by defining a new class that references the parent class in its definition.
# Inheritance is used to create a variation of an objects.
# Parent Class is the class where we inherit all the Function and Attributes they are also called the Base Class or the Super Class.
# Child Class are the variation of the Parent Class they have the same function and attributes,
    # but the Child Class has the ability to have their own functions and attributes that the Parent Class doesn't have.

# Example of Inheritance
class Character:                                    # Parent Class
    def __init__(self, name, hp, mp, atk, lvl):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.lvl = lvl
        
    def created(self):
        print ("Character Created!" + "\nCharacter Name: " + self.name) # Print if the character is being created

    def attack(self):  # Object function to perform an attack action
        print(f"{self.name} attacks with {self.atk} damage!")  # Print attack message
    
    def level_up(self):  # Object function to level up the character
        self.lvl += 1  # Increase the level by 1
        print(f"{self.name} has leveled up to level {self.lvl}!")  # Print level up message

class Type(Character):              # Child Class
    def __init__(self, name, hp, mp, atk, lvl, jobType):
        super().__init__(name, hp, mp, atk, lvl)
        self.jobType = jobType
        
    def withjobType(self):
        super().created()
        print ("Job Type: " + self.jobType)  # add a jobType when a character is created


typeOne = Type("Arjay", 100, 50, 12, 1, "Swordsman")  # Create an instance of Character using Child Class with specific values
typeOne.withjobType()
typeOne.attack()
typeOne.level_up()