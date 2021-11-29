#Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
# и яка вертатиме True, якщо це число просте, и False - якщо ні.
number = int(input('Write number:'))

def is_prime():
 if 1 < number < 1000:
     for i in range(2, int(number/2)+1):
          if (number % i) == 0:
             return "false"
             break
     else:
         return "true"

 else:
     return "error"
a = is_prime()
print(a)