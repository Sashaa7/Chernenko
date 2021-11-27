#Написати функцію < bank > , яка працює за наступною логікою:
#користувач робить вклад у розмірі < a > одиниць строком на < years > років під < percents > відсотків 
#(кожен рік сума вкладу збільшується на цей відсоток,
# ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
#  Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%).
#  Функція повинна принтануть і вернуть суму, яка буде на рахунку.

def bank():
	vklad = int(input('Write how much money your wont invest:'))
	percents = int(input('How much percent  you will have:'))
	years = int(input('How much years you have for invest:'))
	earning =(vklad * ((1 + percents/100)**years))
	print(earning)
bank()