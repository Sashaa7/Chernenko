#Написати скрипт, який отримує від користувача позитивне ціле число і створює словник, з ключами від 0 до введеного числа,
#   а значення для цих ключів - це квадрат ключа.
#        Приклад виводу при введеному значенні 5 :
#        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

user_number =int(input("Write your number"))
our_dictionary = dict()

for x in range(0, user_number + 1):
    our_dictionary[x]=x*x

print(our_dictionary)  