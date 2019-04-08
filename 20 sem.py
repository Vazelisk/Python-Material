import re

def parcer():
    with open('test.xml', encoding='utf-8') as f:
        text = f.read()
    match = re.search('<se>(.+)</se>', text, flags=re.DOTALL | re.MULTILINE)
    match = match.group(1)
    splitted_match = match.splitlines()
    counter = len(splitted_match) - 1
    return counter

def main():
    x = parcer()
    print(x)

if __name__ == '__main__':
    main()
