from instream import InStream
from symboltable import SymbolTable
import stdio
def main():
    instream = InStream('misspellings.txt')
    lines = instream.readAllLines()
    misspellings = SymbolTable()
    for line in lines:
        tokens = line.split(' ')
        misspellings[tokens[0]] = tokens[1]
    while not stdio.isEmpty():
        word = stdio.readString()
        if word in misspellings:
            stdio.write(word + '-->' + misspellings[word])
if __name__ == '__main__':
    main()