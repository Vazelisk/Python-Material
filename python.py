

import os
import re

INPUT_DIR = './files'
OUTPUT_DIR = './final'

def get_texts():
    names = []
    for name in os.listdir(INPUT_DIR):
        name = os.path.join('files', name)
        names.append(name)
    return names

def parcer(names):
    for i in names:
        with open(i, encoding='utf-8') as fh:
            text = fh.read()
        match = re.findall(r'# newdoc id = (\S+)\n((:?(?!# newdoc).*\n)+)', text, flags=re.DOTALL)
    


def main():
    names = get_texts()
    print(names)
    matcher = parcer(names)
    

main()
