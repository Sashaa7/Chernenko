 #Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року
 # якiй цей мiсяць належить (зима, весна, лiто або осiнь)

write_month_number = int(input())

def season():
  
    if  1 <= write_month_number <= 2 or write_month_number == 12:
       print('winter')

    if 3 <= write_month_number <= 5:
      print('spring')

    if 6 <= write_month_number <= 8:
      print('summer')

    if 9 <= write_month_number <= 11:
      print('autumn')
season()