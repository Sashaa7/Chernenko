#Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку
#Тобто, функція приймає два аргументи: список і величину зсуву
 #(якщо ця величина додатня - пересуваємо з кінця на початок,
 # якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
 #  Наприклад:
 #      fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
 #      fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
our_list = [1, 2, 3, 4, 5]
number = int(input('Write number:'))

def shift(our_list, number):
    if number < 0:
        number = abs(number)
        for i in range(number):
            our_list.append(lst.pop(0))
    else:
        for i in range(number):
            our_list.insert(0, our_list.pop())

shift(our_list, number)
print(our_list)