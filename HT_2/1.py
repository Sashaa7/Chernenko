#Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".
#Елементами списку повинні бути як рядки, так і числа.

my_list = [1, 223, 'sasha', 'red', 'foo', 123123, 'monday']

my_list_str = ''.join(map(str, my_list))

print(my_list_str)