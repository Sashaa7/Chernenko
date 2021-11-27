#Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата,
#і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.

side = int(input('Enter  length of the side square:'))

def square():
    print('Perymetr:',4 * side)
    print('Ploscha:',side ** 2)
    print('Diagonal:',side ** 0.5)
square() 