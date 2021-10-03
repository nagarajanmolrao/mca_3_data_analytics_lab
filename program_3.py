# Write a python program using object oriented programming to demonstrate encapsulation, overloading and inheritance

# ENCAPSULATION
class Apple:

    def __init__(self):
        self.__sellPrice = 50

    def sell(self):
        print("Selling Price: {}".format(self.__sellPrice))

    def setSellPrice(self, price):
        self.__sellPrice = price


print("DEMONSTRATION OF ENCAPSULATION\n")
a = Apple()
a.sell()
# trying to change the price directly
a.__sellPrice = 100
a.sell()
# using set function to change the price
a.setSellPrice(100)
a.sell()


# OVERLOADING
class Banana:

    def __init__(self):
        self.color = "Yellow"
        self.price = 60

    def change(self, color=None, price=None):
        if color is None and price is None:
            self.color = "Yellow"
            self.price = 60
        elif color is not None and price is None:
            self.color = color
        else:
            self.color = color
            self.price = price

    def Bprint(self):
        print("Banana Color : ", self.color)
        print("Banana Price : ", self.price)


print("\nDEMONSTRATION OF OVERLOADING\n")
b = Banana()
b.Bprint()
b.change("Red")
b.Bprint()
b.change("Yellow", 100)
b.Bprint()


# INHERITANCE
class Candidate:

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isStudent(self):
        return False


class Student(Candidate):

    def isStudent(self):
        return True


print("\nDEMONSTRATION OF INHERITANCE\n")
stu1 = Candidate("DummyCandidate")
print(stu1.getName(), stu1.isStudent())
stu2 = Student("WasteCandidate")
print(stu2.getName(), stu2.isStudent())
