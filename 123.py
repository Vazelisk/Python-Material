def text_to_words(file):
    words = []
    file = 'episode1.txt'
    with open(file, encoding='utf-8') as text:
        for line in text:
            line = line.strip()
            if line.startswith('[') and line.endswith(']'):
                continue
            ar = line.split(': ')
            if len(ar) == 1:
                replica = ar[0]
            else:
                actor, replica = ar
            words_in_replica = replica.split()
            words.extend(words_in_replica)
        return words

def main():
    word = input('Введите слово: ') 
    file = 'episode1.txt'
    words = text_to_words(file)
    x = 0
    x = words.count(word)
    print('В диалогах слово', word, 'встречается', x, 'раз')

if __name__ == '__main__':
    main()
