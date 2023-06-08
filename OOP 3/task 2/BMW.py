from base import Car


class BMW(Car):
    def __init__(self, max_speed, model):
        super().__init__(max_speed)
        self.model = model

    def introduce(self):
        return f"The car is {self.model}, Max speed is {self.max_speed} km/h"

