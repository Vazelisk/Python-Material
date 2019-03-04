import re

#() - объединение, запоминает, органичивает
#(?:) - объединение
#

match = re.search(r'^[-+]?\d+\.?\d*$', '+255.')
match1 = re.search(r'^[-+]?((\d*\.?\d+)|(\d+\.?\d*))$', '.2')

if match:
    print(match.group())

if match1:
    print(match1.group())


match = re.search(r'([А-ЯЁ][а-яё]*)\s([IXV]+)', 'Первый император России Петр I')
print(match.group())
print(match.group(0))
print(match.group(1))
print(match.group(2))

match = re.search(r'(\D\d)+', 'a1b2c3')
print(match.group())
print(match.group(1))

+7-999-123-45-67
8-999-123-45-67


match = re.search(r'(?:\+7|8)(?:-\d{3}){2}(?:-(\d{2})){2}', '+7-999-123-45-67')
print(match.group())
# ?: - группа не запоминается
print(match.group(1))

