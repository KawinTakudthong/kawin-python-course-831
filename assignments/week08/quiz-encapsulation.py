"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def getArea(self):
        return self.__length * self.__width

    def getPerimeter(self):
        return 2 * (self.__length + self.__width)

    def isSquare(self):
        if self.__length == self.__width:
            return f"This rectangle is a square."
        else:
            return f"This rectangle is not a square."
        
Rectangle = Rectangle(10, 5)
print(Rectangle.getArea()) 