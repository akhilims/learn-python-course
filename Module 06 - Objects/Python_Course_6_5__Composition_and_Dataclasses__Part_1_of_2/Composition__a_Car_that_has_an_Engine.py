# Composition: a Car that has an Engine
# Every cell of the notebook, in order, as one script (run: python Composition__a_Car_that_has_an_Engine.py)

# ## An Engine class: the part that does the work

class Engine:
    def start(self):
        print("Engine on")

Engine().start()

# ## Composition: a Car creates its own Engine

class Car:
    def __init__(self):
        self.engine = Engine()
    def start(self):
        self.engine.start()

print(type(Car().engine).__name__)

# ## Using the Car: we only talk to the car

c = Car()
c.start()
