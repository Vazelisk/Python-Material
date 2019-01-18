#Арцишевский Антон, 183 группа, 11 дз
import random
vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я', 'А', 'О', 'И', 'Е', 'Ё', 'Э', 'Ы', 'У', 'Ю', 'Я']
def get_words1():
    with open('text1.txt', encoding='utf-8') as fh: #файлы со словами должны лежать в одной папке с программой
        text = fh.read()
    counter1 = 0
    words1 = text.split()
    x1 = random.choice(words1)
    for letter in x1:
        if letter in vowels:
            counter1 += 1
    return x1, counter1

def get_words2():
    with open('text2.txt', encoding='utf-8') as fh:
        text = fh.read()
    counter2 = 0
    words2 = text.split()
    x2 = random.choice(words2)
    for letter in x2:
        if letter in vowels:
            counter2 += 1
    return x2, counter2

def get_words31():
    with open('text3.1.txt', encoding='utf-8') as fh:
        text = fh.read()
    counter31= 0
    words31 = text.split()
    x31 = random.choice(words31)
    for letter in x31:
        if letter in vowels:
            counter31 += 1
    return x31, counter31

def get_words32():
    with open('text3.2.txt', encoding='utf-8') as fh:
        text = fh.read()
    counter32 = 0
    words32 = text.split()
    x32 = random.choice(words32)
    for letter in x32:
        if letter in vowels:
            counter32 += 1
    return x32, counter32

def get_words33():
    with open('text3.3.txt', encoding='utf-8') as fh:
        text = fh.read()
    counter33 = 0
    words33 = text.split()
    x33 = random.choice(words33)
    for letter in x33:
        if letter in vowels:
            counter33 += 1
    return x33, counter33

def line1():
    x1 = get_words1()
    x2 = get_words2()
    x3 = get_words31()
    if x1[1] + x2[1] + x3[1] != 5 or x1[1] + x2[1] != 5 or x1[1] != 5:
        while x1[1] + x2[1] + x3[1] != 5 or x1[1] + x2[1] != 5 or x1[1] != 5:
            x1 = get_words1()
            x2 = get_words2()
            x3 = get_words31()
            if x1[1] + x2[1] + x3[1] == 5 or x1[1] + x2[1] == 5 or x1[1] == 5:
                break
    if x1[1] + x2[1] + x3[1] == 5:
        lineone = x1[0] + ' ' + x2[0] + ' ' + x3[0] + '.'
        return lineone
    elif x1[1] + x2[1] == 5:
        lineone = x1[0] + ' ' + x2[0] + '.'
        return lineone
    elif x1[1] == 5:
        lineone = x1[0] + '.'
        return lineone

def line2():
    x1 = get_words1()
    x2 = get_words2()
    x3 = get_words31()
    if x1[1] + x2[1] + x3[1] != 7 or x1[1] + x2[1] != 7 or x1[1] != 7:
        while x1[1] + x2[1] + x3[1] != 7 or x1[1] + x2[1] != 7 or x1[1] != 7:
            x1 = get_words1()
            x2 = get_words2()
            x3 = get_words32()
            if x1[1] + x2[1] + x3[1] == 7 or x1[1] + x2[1] == 7 or x1[1] == 7:
                break
    if x1[1] + x2[1] + x3[1] == 7:
        linetwo = x1[0] + ' ' + x2[0] + ' ' + x3[0] + '.'
        return linetwo
    elif x1[1] + x2[1] == 7:
        linetwo = x1[0] + ' ' + x2[0] + '.'
        return linetwo
    elif x1[1] == 7:
        linetwo = x1[0] + '.'
        return linetwo

def line3():
    x1 = get_words1()
    x2 = get_words2()
    x3 = get_words31()
    if x1[1] + x2[1] + x3[1] != 5 or x1[1] + x2[1] != 5 or x1[1] != 5:
        while x1[1] + x2[1] + x3[1] != 5 or x1[1] + x2[1] != 5 or x1[1] != 5:
            x1 = get_words1()
            x2 = get_words2()
            x3 = get_words33()
            if x1[1] + x2[1] + x3[1] == 5 or x1[1] + x2[1] == 5 or x1[1] == 5:
                break
    if x1[1] + x2[1] + x3[1] == 5:
        linethree = x1[0] + ' ' + x2[0] + ' ' + x3[0] + '.'
        return linethree
    elif x1[1] + x2[1] == 5:
        linethree = x1[0] + ' ' + x2[0] + '.'
        return linethree
    elif x1[1] == 5:
        linethree = x1[0] + '.'
        return linethree

def main():
    print(line1())
    print(line2())
    print(line3())

if __name__ == '__main__':
    main()