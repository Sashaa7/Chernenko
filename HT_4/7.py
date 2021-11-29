#Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
def our_function():
  our_list = [1, 2, 5, 7, 11, 2, 5, 6, 5, 5, "a", "b", "a", (1, 2), (1, 2), (5, "s")]
  changed_list = set(our_list)
  result={}
  for i in changed_list:
      result[i]=our_list.count(i)
  print(result)
our_function()