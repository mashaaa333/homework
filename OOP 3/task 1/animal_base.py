class Animal:
    def __init__(self, type_,name, foot_count):
        self.type_ = type_
        self.foot_count = foot_count
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name} I am {self.type_}, and I have {self.foot_count} feet")

