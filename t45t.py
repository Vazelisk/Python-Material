#{3,} #от 3 до бесконечности
#{k,n} #от k до n раз встречается что-то
#[^abc.] #отрицание - не найти а или б или с или ???
#+?, *? - щедрое регвыр (найди 1/0 раз, но чем меньше, тем лучше)

import re

print(re.search('a', 'abc'))
print(re.search('bcd', 'abc'))

match = re.search(r'\d', 'abc')
if match: #Если что-то нашлось
    print(match.group())
else:
    print('Ничего не найдено')

match = re.search(r'\d{1,2}\s\w+\s\d{4}\sгода', '18 мая 1956 года')
    #r'[а-яА-ЯёЁ]+-[а-яА-ЯёЁ]+', '')
if match: 
    print(match.group())
else:
    print('Ничего не найдено')

match = re.search(r'\d{1,2}\s\w+\s\d{4}\sгода', """Ранним утром 18 мая 1956 года
    родилась Клара Ивановна""")
if match: 
    print(match.group())
else:
    print('Ничего не найдено')

found = re.findall(r'\S+', """Ранним утром 18 мая 1956 года
    родилась Клара Ивановна""")
print('-'.join(found))


found = re.findall(r'[aA][bB][aA]', 'ababABAb')
print(found)
found = re.findall(r'a*', 'aaaaaa')
print(found)
