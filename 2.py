import collections

d = {'Василиса': ['ручка', 'ручка', 'ножницы', 'фломастер'],
     'Вася': ['ручка', 'мелок', 'ластик', 'мелок']}

#student, item = input('Имя ученика и предмет чере пробел: ').split()
#list_of_items = d[student]
#print(list_of_items)
#count = list_of_items.count(item)
#print(count)

#print(collections.Counter(d['Вася']))
#for student, list_of_items in d.items():
#    d[student] = collections.Counter(list_of_items)

#print(d)

#student, item = input('Имя ученика и предмет чере пробел: ').split()
#print(d[student][item])

#item = input('предмет: ')
#count = 0
#for counter in d.values():
#    print(counter)
#    print(counter[item])
#    count += counter[item]
#print(count)

while True:
    input_ = input('ученик предмет: ')
    if input_ == '':
        break
    student, item = input_.split()
    if student not in d:
        d[student] = collections.Counter()
    d[student][item] += 1
pprint.pprint(d)
