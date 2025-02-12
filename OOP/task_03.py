from task_02 import Rectangle

def area(self):
    return self.width * self.height

Rectangle.area = area

rectangle = Rectangle(5, 10)
print(rectangle.area())
