class User:
    def __init__(self, name, lastName, likesCount, friendsName):
        self.name = name
        self.lastName = lastName
        self.likesCount = likesCount
        self.friendsName = friendsName
        print ("User Created " + self.name)
        

    def introduce(self):
        print("Hi, my name is " + self.name + " " + self.lastName + ".")
        
    def fullProfile(self):
        print("Name: " + self.name + " " + self.lastName)
        print("Likes Count: " + str(self.likesCount))
        print("Friends:")
        for friends in self.friendsName:
            print("   -" + friends)

userOne = User("Arjay", "Sto. Domingo", 100, ["Thily", "Cyndi"])
userOne.introduce()
userOne.fullProfile()