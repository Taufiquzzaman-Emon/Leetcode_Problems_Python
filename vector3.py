'''Write __str__() method to print the vector as follows:
 7i + 8j +10k
Assume vector of dimension 3 for this problem.'''

class ThreeDVector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
# other is used because if we use a second vector the two vectors can be added
    def __add__(self, other):
        return ThreeDVector(self.i + other.i, self.j + other.j, self.k + other.k)

    def show(self):
        print(f"The 3D vector is {self.i}i + {self.j}j + {self.k}k")
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
i = int(input("Enter the value of i: "))
j = int(input("Enter the value of j: "))
k = int(input("Enter the value of k: "))

i2 = int(input("Enter the value of i for the second vector: "))
j2 = int(input("Enter the value of j for the second vector: "))
k2 = int(input("Enter the value of k for the second vector: "))

i3 = int(input("Enter the value of i for the second vector: "))
j3 = int(input("Enter the value of j for the second vector: "))
k3 = int(input("Enter the value of k for the second vector: "))

vector2 = ThreeDVector(i2, j2, k2)  # This is the second vector (other)
vector3 = ThreeDVector(i3, j3, k3)  # This is the second vector (other)


Vector1 = ThreeDVector(i,j,k)
vector = Vector1 + vector2 +vector3
vector.show()