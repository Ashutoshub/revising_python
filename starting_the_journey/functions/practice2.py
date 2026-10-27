import math
def circle_stats(r):
    area = math.pi * r * r
    circumference = math.pi * 2* r
    return area , circumference
a,c = circle_stats(45)
print("Area is: ", a)
print("Circumference is: ", c)