def square(side):
    area = side * side
    if not isinstance(area, int):
        area = int(round(area))
    return area
side = 5.6
result = square(side)
print("Площадь квадрата со стороной", side, "равна:", result)