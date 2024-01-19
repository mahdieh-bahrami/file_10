class Operator:
    def __init__(self, x):
        self.x = x
    def __mul__(self, other):
        R = self.x * other.x
        return R
    def __truediv__(self, other):
        R = self.x / other.x
        return R
    def __sub__(self, other):
        R = self.x - other.x
        return R
# 
n = float(input("enter number 1 : "))
m = float(input("enter number 2 : "))
# 
object1 = Operator(n)
object2 = Operator(m)
print()
print(f"Multiplication : {object1 * object2}")
print(f"Division       : {object1 / object2}")
print(f"Subtraction    : {object1 - object2}")