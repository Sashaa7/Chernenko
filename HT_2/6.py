#Написати скрипт, який об'єднає три словника в самий перший. Оновлюється тільки перший словник. Дані можна "захардкодити".
#        Sample Dictionary :
#        dict_1 = {1:10, 2:20}
#        dict_2 = {3:30, 4:40}
#        dict_3 = {5:50, 6:60}
#        Expected Result : dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dict_1 = {1:1340, 2:223}

dict_2 = {3:305, 4:42340}

dict_3 = {5:5450, 6:6045}

update_our_dictionary_1 = dict_1.update(dict_2) 
update_our_dictionary_2 = dict_1.update(dict_3)
print(dict_1)