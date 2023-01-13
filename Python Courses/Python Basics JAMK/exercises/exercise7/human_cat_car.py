import random
from human_class import Human
from cat_class import Cat
from car_class import Car


adam = Human("Adam", "18")
eve = Human("Eve", "18")

print(adam)
print(eve)

###

kit = Cat("Kit", "orange")
katsi = Cat("Katsi", "black")

print(kit)
print(katsi)
print(kit.meow())
print(katsi.meow())


###

car1 = Car("Skoda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)

print("Car 1: ", car1)
print("Car 2: ", car2)
print("Car 3: ", car3)
print("Total price of your cars is: ", car1.price + car2.price + car3.price)

###

car4 = Car("Audi", "XV22", random.randint(1000, 10000))
car5 = Car("BMW", "XV8", random.randint(1000, 10000))
car6 = Car("Ford", "XV88",random.randint(1000, 10000))
car7 = Car("Opel", "XV104", random.randint(1000, 10000))
car8 = Car("Skoda", "XV8-05", random.randint(1000, 10000))

print("Car 4: ", car4)
print("Car 5: ", car5)
print("Car 6: ", car6)
print("Car 7: ", car7)
print("Car 8: ", car8)
