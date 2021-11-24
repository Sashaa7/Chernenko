#Ну і традиційно -> калькулятор :)
#повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

first_number = int(input('Write your number:'))

symbol = input('Write what are you want to do: +, -, * or /:')

the_last_number = int(input('Write second number:'))

def calculator():
	if symbol == '+':
		print(first_number + the_last_number)
	if symbol == '-':
		print(first_number - the_last_number)
	if symbol == '*':
		print(first_number * the_last_number)
	if symbol == '/':
		print(first_number / the_last_number)
		
calculator()