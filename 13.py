# 13. Дано четырехзначное число. Поменяйте местами наименьшую и наибольшую цифры.


a = input('Введите четырёхзначное натуральное число: ')
i = 0
x = 0
y = 0
if a.isdigit():                          #Проверяется что дано число
    if len(a) == 4:                      #Проверка на необходимое количество знаков в строке
        #a = int(a)                       #Преобразование строки в целое число
        for i in range(len(a)):

    else:
        print('Введено неверное количество знаков!!!')
else:
    print('НЕКОРРЕКТНЫЙ ВВОД!!!')
