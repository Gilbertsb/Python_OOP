class Vehicle:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand

    def movemt(self):
        print("MOVE")

class Car(Vehicle):
    def move(self):
        print("drive")
    
class Plane(Vehicle):
    def move(self):
        print("Fly")

car1=Car("Toyota","Rava4")
plan1=Car("Bombadier","B6768")

#  print(car1.model)
#  print(car1.brand)
for i in (car1,plan1):
    print(i.model)
    print(i.brand)


