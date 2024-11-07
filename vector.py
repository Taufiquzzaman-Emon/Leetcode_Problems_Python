# chapter 11 (Inheritence
'''Create a class (2-D vector) and use it to create another class representing a 3-D
vector.
'''
class TwoDVector:
    
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The 2D Vector is: {i_2d}i+{j_2d}j")

class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"The 3D Vector is: {i_3d}i+{j_3d}j+{k_3d}k")


i_2d = int(input("Enter the value of i for 2D vector: "))
j_2d = int(input("Enter the value of j for 2D vector: "))

two = TwoDVector(i_2d, j_2d)
two.show()

# Input for 3D Vector (separate from 2D Vector)
i_3d = int(input("Enter the value of i for 3D vector: "))
j_3d = int(input("Enter the value of j for 3D vector: "))
k_3d = int(input("Enter the value of k for 3D vector: "))

three = ThreeDVector(i_3d, j_3d, k_3d)
three.show()



        
