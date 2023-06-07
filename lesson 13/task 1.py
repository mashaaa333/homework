class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def surface(self):
        return 2 * (self.width + self.length)

rectangle = Rectangle(length=int(input("Input length: ")), width=int(input("Input width: ")))
answer_area = rectangle.area()
answer_surface = rectangle.surface()
print("Surface:", answer_surface)
print("Area:", answer_area)
