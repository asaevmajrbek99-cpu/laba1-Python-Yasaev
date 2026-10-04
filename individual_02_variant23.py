print("Введите значения ширины и высоты листа.")
width = float(input("Ширана = "))
height = float(input("Высота = "))
print("Введите длину стороны квадрата.")
side =  float(input("Сторона квадрата = "))

#количество квадратов по ширине
cols = width // side
#количество квадратов по высоте
rows = height // side

#максимальное число квадартов
count = cols * rows

#площадь неиспользованной части
ploshad = width * height - count * side * side

print(f"Максимальное число квадратов:{count}; Площадь неиспользованной территории {ploshad}")

