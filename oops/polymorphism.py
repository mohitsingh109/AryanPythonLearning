# Same function name, but different behaviour

class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")

shapes = [Circle(), Square(), Triangle()]

for shape in shapes:
    shape.draw()