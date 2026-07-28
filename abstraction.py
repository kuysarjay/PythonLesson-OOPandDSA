# Abstraction is the process of hiding implementation details and exposing only the essential
# functionality to the user.
# It is used to hide the implementation details from the user and expose only necessary parts,
# making the code simpler and easier to interact with.

# Abstract Base Class (ABC) is used to achieve data abstraction by defining a common interface for its subclasses.
# It cannot be instantiated directly and serves as a blueprint for other classes.
# Abstract classes are created using abc module and @abstractmethod decorator,
# allowing developers to enforce method implementation in subclasses while hiding complex internal logic.

from abc import ABC, abstractmethod

# Example:
class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method

class English(Greet):
    def say_hello(self):
        return "Hello!"

english = English()
print(english.say_hello())

# Components of Abstraction
# Abstraction is made up of key components that define a clear and enforced structure for subclasses
# while hiding unnecessary implementation details.

# 1. Abstract Method
# Abstract methods are method declarations without a body defined inside an abstract class.
# They act as placeholders that force subclasses to provide their own specific implementation,
# ensuring consistent structure across derived classes.

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method, no implementation here

# 2. Concrete Method
# Concrete methods are fully implemented methods within an abstract class.
# Subclasses can inherit and use them directly, promoting code reuse without needing to redefine common functionality.

class AnimalWithMove(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def move(self):
        return "Moving"

class Dog(AnimalWithMove):
    def make_sound(self):
        return "Bark"

dog = Dog()
print(dog.move())

# 3. Abstract Properties
# Abstract properties work like abstract methods but are used for properties.
# These properties are declared with @property decorator and marked as abstract using @abstractmethod.
# Subclasses must implement these properties.

class AnimalWithSpecies(ABC):
    @property
    @abstractmethod
    def species(self):
        pass

class Cat(AnimalWithSpecies):
    @property
    def species(self):
        return "Feline"

cat = Cat()
print(cat.species)

# 4. Abstract Class Instantiation
# Abstract classes cannot be instantiated directly.
# This is because they contain one or more abstract methods or properties that lack implementations.
# Attempting to instantiate an abstract class results in a TypeError.

# The following code is intentionally commented out because it would raise TypeError:
'''
class IncompleteAnimal(ABC):
     @abstractmethod
     def make_sound(self):
         pass

 animal = IncompleteAnimal()
'''