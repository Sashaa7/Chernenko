#Вводиться число. Якщо це число додатне, знайти його квадрат,
#якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
number = int(input('Write your number:'))

def our_function(number):
	if number < 0:
		print(number + 100)
	if number > 0:
		print(number ** 2)
	if number == 0:
		print(number)
our_function(number)
