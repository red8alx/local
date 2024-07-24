class Car:
    def __init__(self, engine):
        self.engine = engine
    def start(self):
        self.engine.start()
class Engine:
    def start(self):
        print("Engine is starting...")
my_car = Car(Engine())
my_car.start()