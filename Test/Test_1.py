# a = 'Paradise'
# print(''.join(reversed(list(a))))


lst = ['hello', 'world', '123']
x = input('Enter: ')
if x in lst:
    i = lst.index(x)
else:
    x = -1
print(x)