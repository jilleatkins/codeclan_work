from modules.car import *
from modules.engine import *
from modules.gearbox import *

Engine = engine(2)
Gearbox = gearbox(6)

Car = car("red", "Ford", Engine, Gearbox)

print(Car.colour)
print(Car.engine.volume)
print(Car.engine.ignite())