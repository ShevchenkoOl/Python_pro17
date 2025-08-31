# a = 5
# b = "Hello"
# a + b   # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print("Hello!")

# ZeroDivisionError: division by zero

botle_of_beer = 10

try:
    people = int(input("Введите количество человек которые будут на вечеринке: "))
    if people < 0:
        print("Количество людей должно быть больше нуля")
    else:
        botle_for_peolpe = botle_of_beer / people
        print(botle_for_peolpe)
except ZeroDivisionError:
    print("Поскольку вас ноль, вечеринка не состоиться")
except ValueError:
    print("Вы ввели не число, количество людей измеряеться в целых числах")
except TypeError:
    print("Вы ввели не число, количество людей измеряеться в целых числах")
else:
    print("К счастью ошибок не виявлено!")
finally:
    print("Вечеринка состоиться в любом случаи 🫶")

    
    
print("Hello")