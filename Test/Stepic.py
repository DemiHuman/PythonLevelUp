# Напишите программу, которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a;b], которые делятся на 3.
#
# В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [−5;12].
# Всего чисел, делящихся на 3, на этом отрезке 6: −3,0,3,6,9,12. Их среднее арифметическое равно 4.5
#
# На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3.

a = int(input('Первое число: '))
b = int(input('Второе число: '))
x = 0
y = 0

sp = (int(i) for i in range(a, b+1) if not i % 3)
print(list(sp))

for i in enumerate(sp):
    if i[a] == 0:
        continue
    else:
        x += i
        print(x)
        y += 1
        print(y)

z = x / y
print(z)


# for i in range(a, b+1):
#     if i % 3 == 0:
#         y += 1
#         print(y)
#         x += i
#         print(x)
#
#