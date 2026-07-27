# Polymorphism is another important concept of object-oriented programming.
# It simply means more than one form.
# That is, the same entity (method or operator or object)
    # can perform different operations in different scenarios.
# The main purpose of the render() method is to render the shape.
# However, the process of rendering a square is different from the process of rendering a circle.

# Example of Polymophism:
class Polygon:
    # method to render a shape
    def render(self):
        print("Rendering Polygon...")

class Square(Polygon):
    # renders Square
    def render(self):
        print("Rendering Square...")

class Circle(Polygon):
    # renders circle
    def render(self):
        print("Rendering Circle...")
    
# create an object of Square
s1 = Square()
s1.render()

# create an object of Circle
c1 = Circle()
c1.render()