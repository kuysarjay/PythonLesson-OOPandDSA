# Object-Oriented Programming - it aims to implement real world objects / entities its attributes
    # and behavior into Programming so that we can represent it in out game, software or applications.

# Object - anything that has an attribute and a purpose is an object.
    # e.g: Game Character, Real-Life People (Students, Employees, etc.), Real-Life Object (Fruits, Tables, etc.)
# Class - used in Programming to make a blueprint for our project. It will represent attribute and purpose.
    # e.g: Game Character                           # Product
            # Purpose                                   # Purpose
                # Physical Attack                           # Restock
                # Magical Attack                            # Adjust
            # Attribute                                     # Delete
                # Name                                  # Attribute
                # HP                                        # ID
                # MP                                        # Name
                # Attack                                    # Price
                # Level                                     # Quantity
                
# Example of Class and Object

class Character:
    name = "Name"       # Default value of the class
    hp = 100
    mp = 50
    atk = 12
    lvl = 1
    
charOne = Character()   # we create the two character
charTwo = Character()

charOne.name = "Arjay"  # changing the name of character 1
print(charOne.name)