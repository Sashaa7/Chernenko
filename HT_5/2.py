 #Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
 #  - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
 #  - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
 #  - щось своє :)
 #  Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.

def our_function():
  name = input('Please write your name:')
  password = input('Write your password:')
  if 3 < len(name) < 50 and if 8 < len(password):
    print('Data is entered correctly')
  else:
    
our_function()