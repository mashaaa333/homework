from BMW import BMW
from Ferrari import Ferrari

bmw_car = BMW(max_speed=250, model="BMW X5")
ferrari_car = Ferrari(max_speed=350, model="Ferrari 488 GTB")

print(f"BMW Car: {bmw_car.introduce()}")

print(f"Ferrari Car: {ferrari_car.introduce()}")
