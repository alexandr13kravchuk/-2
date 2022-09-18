from math import sqrt
 
def distance(up, left, down, right):
    return sqrt((up-down) ** 2+(left-right) ** 2)
 
up=int(input("Сделай шаги вверх робот\n"))
down=int(input("Сделай шаги вниз робот\n"))
left=int(input("Сделай шаги влево робот\n"))
right=int(input("Сделай шаги вправо робот\n"))
print("Робот прошёл\n")
print(distance(up, down, left, right))