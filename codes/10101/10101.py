# 10101 삼각형 외우기

x = int(input())
y = int(input())
z = int(input())

if x == y == z == 60:
    print("Equilateral")
elif x + y + z == 180 and (x == y or y == z or x == z):
    print("Isosceles")
elif x + y + z == 180 and (x != y and y != z and x != z):
    print("Scalene")
else:
    print("Error")