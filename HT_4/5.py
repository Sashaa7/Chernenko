# Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci():
	fib_1 = 1
	fib_2 = 1
	fib_all = fib_1 + fib_2
	number = int(input('Write number:'))
	if number > 0:
		print(fib_1)
		print(fib_2)
	while fib_all <= number:
		print(fib_all)
		fib_1 = fib_2
		fib_2 = fib_all
		fib_all = fib_1 + fib_2
fibonacci()