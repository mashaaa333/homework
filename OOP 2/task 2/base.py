import perimeter_area_volume

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def display(self):
        area = perimeter_area_volume.Area(self.length, self.width).area()
        perimeter = perimeter_area_volume.Perimeter(self.length, self.width).perimeter()
        volume = perimeter_area_volume.Parallelepiped(self.length, self.width, 4).volume()
        print(f"The area is {area},\n The perimeter is {perimeter},\n The volume is {volume}")
