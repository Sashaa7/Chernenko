# Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
#-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
#-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
#-  якщо довжина бульше 50 - > ваша фантазiя

ryadok = input()

number_of_characters = len(ryadok)

def our_function():
  if 30 < number_of_characters < 50:
    print(number_of_characters)
  
  if number_of_characters < 30:
    for symbol in ryadok:
      if symbol.isalpha():
        print(symbol, end = "")
    
  if number_of_characters > 50:
    print('Hello world!')

our_function()

