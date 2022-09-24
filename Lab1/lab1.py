import math

def is_choice_invalid(choice):
    return not (choice in ['Г', 'Р'])

def convert(num, is_degree):
    return math.radians(num) if is_degree else math.degrees(num)
    
def is_number_invalid(num):
    try:
        float(num)
        return False
    except ValueError:
        return True

choice = input('Введіть одиницю вимірювання (Г - градуси, Р - радіани): ')

while (is_choice_invalid(choice.strip())):
    choice = input('Введене значення неправильне. Введіть одиницю вимірювання ще раз (Г - градуси, Р - радіани): ')
is_degree = choice == 'Г'

value = input('Введіть значення величини кута: ')
while (is_number_invalid(value)):
    value = input('Введене значення неправильне. Введіть значення величини кута ще раз: ')


converted_value = round(convert(float(value), is_degree), 2)
print('Значення у ' + ('радіанах: ' if is_degree else 'градусах: '), converted_value)


