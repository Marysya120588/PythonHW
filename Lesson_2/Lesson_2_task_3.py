from math import ceil

def square(a):
    s = a ** 2
    return s

a = float(input("Длина стороны квадрата: "))
result = square(a)
rounded_result = ceil(result)
print(f'Округлённая в большую сторону площадь - {rounded_result}')