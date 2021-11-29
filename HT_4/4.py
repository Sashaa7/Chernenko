#Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
# і вертатиме список простих чисел всередині цього діапазона.

first_number = int(input('Write first number:'))
second_number = int(input('Write second number:'))
new_list = []

def prime_list():
  for i in range(first_number, second_number):
 
      for j in range(2,i):
          if i%j==0:
              break
 
      else:  
          new_list.append(i)
 
  return new_list
a = prime_list()
print(a)
