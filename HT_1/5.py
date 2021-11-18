#Write a script to check whether a specified value is contained in a group of values.
#        Test Data :
#        3 -> [1, 5, 8, 3] : True
#        -1 -> (1, 5, 8, 3) : False
a = int(input('Enter a value'))
b = input('Enter a number to check if its in a group')
c = 0
search = b.split()
for i in range(0,len(search)):
  if a== int(search[i]):
    c = 1
 
if c == 1:
  print('True')
else:
  print('False') 