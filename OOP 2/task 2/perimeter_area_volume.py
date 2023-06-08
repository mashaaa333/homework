from base import Rectangle


class Perimeter(Rectangle):
    def perimeter(self):
        return self.width * 2 + self.length * 2


class Area(Rectangle):
    def area(self):
        return 2 * (self.length + self.width)


class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.width * self.length * self.height
