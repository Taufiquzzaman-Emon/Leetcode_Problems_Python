'''Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
‘Pets’. Add a method ‘bark’ to class ‘Dog’.'''

class Animals:
    def __init__(self,a1,a2,a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        
class Pets(Animals):
    pass


class Dogs(Pets):
    def bark(self):
        if self.a1 == "dog" or self.a2 == "dog" or self.a3 == "dog":
            print(f"The {self.a1 or self.a2 or self.a3} barks")
        else:
            print("None of the animals is a Dog, so no barking.")

p1 = (input("Enter the name of the Pet: "))
p2 = (input("Enter the name of pet 2: "))
p3 = (input("Enter the name of pet 3: "))

animal = Dogs(p1,p2,p3)
animal.bark()