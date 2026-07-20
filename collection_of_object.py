# Collection of Object means grouping multiple instances of a class together inside a container like a list, set, or dictionary.
    # This lets you manage and process many objects at once instead of handling them individually
    
# Example of Collection of Object:
class Character:
    def __init__(self, name, hp, mp, atk, lvl):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.lvl = lvl
        
    def createCharacter(self):
        print("\n=================================")
        print("       Character Created!")
        print("=================================")
        
class Type(Character):
    def __init__(self, name, hp, mp, atk, lvl, jobType):
        super().__init__(name, hp, mp, atk, lvl)
        self.jobType = jobType
        
    def withJobType(self):
        super().createCharacter()
        print("Name     : " + self.name)
        print("Job Type : " + self.jobType)
        print("HP       : " + str(self.hp))
        print("MP       : " + str(self.mp))
        print("Attack   : " + str(self.atk))
        print("Level    : " + str(self.lvl))
        
listofCharacter = []

while True:
    print("==================================")
    name = input("Enter your Name: ")
    jobType = input("Select a Job [Swordsman, Mage, Assassin, Healer, Fighter]: ")
    print("==================================")
    
    char = Type(name = name, hp = 100, mp = 20, atk = 35, lvl = 1, jobType = jobType)
    listofCharacter.append(char)
    
    choice = input("Create another Character? [Y/Any char...]: ")
    if choice == 'Y' or choice == 'y': pass
    else: break

for char in listofCharacter:
    char.withJobType()