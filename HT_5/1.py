#Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
 #  Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> 
 #(значення за замовчуванням - <False>).
  # Логіка наступна:
#якщо введено коректну пару ім'я/пароль - вертається <True>;
#якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, 
#`інакше (<silent> == <False>) - породжується виключення LoginException

def our_function():
   our_data = {'Andrey': '12345678', 'Sasha': 'qwertyui', 'Vova': '1234qwert', 'Dima': '4321rewq', 'Petro': 'qwaszx1234'}
   name = input('Write your name:')
   password = input('Write your password:')
   if {name: password} = our_data:
      print('true')
   else:
      print('false')


our_function()

