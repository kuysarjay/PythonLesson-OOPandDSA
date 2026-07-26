# A method is a function embedded inside a class. 
    # The first (or only) parameter of each method is usually named self,
    # which is designed to identify the object for which the method is invoked in order
    # to access the object's properties or invoke its methods.
# If a class contains a constructor (a method named __init__) 
    # cannot return any value and cannot be invoked directly.
# All classes (but not objects) contain a property named __name__,
    # which stores the name of the class. Additionally, a property named __module__ stores
    # the name of the module in which the class has been declared,
    # while the property named __bases__ is a tuple containing a class's superclasses.

# Example of Method:
class Sample:
    def __init__(self):
        self.name = Sample.__name__
    def myself(self):
        print("My name is " + self.name + " living in a " + Sample.__module__)


obj = Sample()
obj.myself()


