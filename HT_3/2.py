#Користувачем вводиться початковий і кінцевий рік. 
#Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).

first_year = int(input('Write the first year:'))

the_last_year = int(input('Write the last year:'))

for num in range(first_year,the_last_year + 1):
    if all(num % 400 == 0 or num %  4 == 0 and num % 100 != 0 for i in range(first_year ,num)):
       print (num)