# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    def drive(self, b="vrooom"):
        print(b)

    def __repr__(self, num_wheels=4):
        return "number of wheels:" + str(num_wheels)



# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        super().__init__(num_wheels)
        self.num_wheels = num_wheels

    def drive(self, b="BRAAAP!!"):
        super().drive(b)

    def __repr__(self, num_wheels=2):
        return "number of wheels:" + str(num_wheels)

myG = GroundVehicle()
myM = Motorcycle()
myG.drive()
myM.drive()
print("GroundVehicle:", myG)
print("Motorchcyle:", myM)
vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]
vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

def mylist1(list):
    for i in vehicles:
        mylist = [i.drive()]
    return mylist


mylist1(vehicles)
