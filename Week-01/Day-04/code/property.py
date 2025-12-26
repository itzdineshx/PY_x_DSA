# Proprty Decorator - defines a method as a property(acessed like an attribute)
# @property.getter, @property.setter, @property.deleter
class Rectangle:
    def __init__(self, width, height):
        # Private attributes
        self._width = width
        self._height = height

    # getter methods
    @property
    def width(self):
        return f"{self._width:.2f} cm"
    @property
    def height(self):
        return f"{self._height:.2f} cm"
    

    # setter methods
    @width.setter
    def width(self, n_width):
        if n_width > 0:
            self._width = n_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, n_height):
        if n_height > 0:
            self._height = n_height
        else:
            print("Height must be greater than zero")


    # delter methods
    @width.deleter
    def width(self):
        del self._width
        print("The width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("The Height has been deleted")

rectangle = Rectangle(3, 3)

print(rectangle.width)
print(rectangle.height)

del rectangle.height