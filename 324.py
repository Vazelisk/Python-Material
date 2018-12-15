a = list(range(7))
print(a)
a.append(6.66) #добавляет только элементы в конец
a.extend(range(7, 10)) #может добавлять операции
print(a)
a.remove(0)#удаляет первое найденное значение
print(a)
x = a.pop(0)#по индексу
a[5] = -100
del a[0]
print(a, x)
print(a[::3])
a.sort()
print(a)

b = (1, 2, 3, 'abc')
#del b[1]
# b[1] = 20
print(b)
print(b[1::]) #порождает новый кортеж
b = ()
print(b)
b = tuple()
print(b)
b = (tuple(a))
print(b)
b = tuple('abc')
print(b)
b = tuple(range(5))
print(b)
x = (5,) #train comma - висящая запятая, позволяет сделать кортеж
print(x)

b = (
    'erwrwer',
    'htrew',
    'ewrewrewr',
)
for x in b:
    print(x)

x, y = [1, 2]
print(x, y)
x, y = y, x #неявное создание кортежа, плохо
print(x, y)

t = (y, x) #нормальное создание кортежа
print(t)
x, y = t
print(t)
b = (1, 2)
print(b, type(b))

def parse_line(line):
    """Извлекает слово и антоним"""
    word, definition, antonyme, example = line.split('|')
    return word, antonyme

s = 'питон|змий|паскаль|П. лучше паскаля'
word, antonyme = parse_line(s)
print(word)
print(antonyme)
t = parse_line(s)
print(t, type(t))
antonyme = parse_line(s)[1] #не очень желательно
print(antonyme)
_, antonyme = parse_line(s)
print(_)

def g():
    return 1, 2, 3

_, x, _ = g()
print(x)

def hello():
    print('hello')

x = hello()
print(x)
if x is None:
    print('x is None')

#Именованные переменные
print('abc', 'def', end='\n#####\n', sep=',')
s = 'Алла: Я купила фруктов: мандарины, икру, яблоки'
name, text = s.split(': ', maxsplit=1)
print(name)
print(text)
name, text = s.split(sep=': ', maxsplit=1)
print(name)
print(text)
name, text = s.split(': ', 1)
print(name)
print(text)
#мы можем опускать аргументы, тогда они определяются по их местоположению
#если указывать имена, то можно располагать в любом порядке
name, text = s.split(maxsplit=1, sep=': ')
print(name)
print(text)
#name, text = s.split(sep=': ', 1) #ошибка синтаксиса, сначала только позиционные

def volume(x, y, z):
    return x * y * z

volume(1, 2, z=3)
print(volume(x=1, y=2, z=3))
print(volume(z=3, x=1, y=2))
#print(volume(x=1, 2, 3)) - сначала позиционные

def volume(x, y, z=1):
    return x*y*z

print(volume(1, 2))

def say_hello(name, status=None):
    if status is None:
        print('Добрый день,', name)
    else:
        print('Добрый день,', status, name)


say_hello('Смит', 'мисс')
say_hello('Фродо')
