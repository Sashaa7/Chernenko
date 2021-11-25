# Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
#-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
#-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
#-  якщо довжина бульше 50 - > ваша фантазiя

my_string = input()
letters_only = []
my_suma = 0
numbers = 0
letters = 0

for symbol in my_string:
  if symbol.isdigit():
    my_suma += int(symbol)
    numbers += 1
  elif symbol.isalpha():
    letters_only += symbol
    letters += 1

if len(my_string) > 30 and len(my_string) < 50:
  print('Дожина:', len(my_string))
  print('Цифри:', numbers)
  print('Букви:', letters)

elif len(my_string) < 30:
  print('Сумма чисел', my_suma)
  print('Рядок без цифр', ''.join(letters_only))

elif len(my_string) > 50:
  print('Hello world')


