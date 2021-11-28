#Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
def our_function():
  our_list = input('Write your list:')
  changed_list = set(our_list)
  result={}
  for i in changed_list:
      result[i]=our_list.count(i)
  print(result)
our_function()