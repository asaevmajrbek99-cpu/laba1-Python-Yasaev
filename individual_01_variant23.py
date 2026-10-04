import math

print("Введите значение катетов: ")

a = float(input("a = "))
b = float(input("b = "))

c = math.sqrt(a**2 + b**2)
с = math.floor(c)
print(f"Гипотенуза = {c}")
print(f"Периметр прямоугольного треугольника = a + b + c = {a + b + c}")
