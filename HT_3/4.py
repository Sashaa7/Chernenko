#Створiть 3 рiзних функцiї (на ваш вибiр). 
#Кожна з цих функцiй повинна повертати якийсь результат. 
#Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат.
#Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3

def function_1():
    print('Hello')

def function_2():
    print('World')

def function_3():
    print('and')

def function_4():
    function_1()
    function_2()
    function_3()
    print('everybody')

function_4()
