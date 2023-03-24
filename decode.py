from letterFrequency import *
from sortWords import *


def decode():
    # Reading the two text files
    refList = []
    with open('wells.txt', 'r', encoding='utf-8') as file:  # opens file as string
        refList = file.read().lower().split()
    cipherText = []
    with open('cipherText-project3.txt', 'r', encoding='utf-8') as file:  # opens file as string
        cipherList = file.read().split()

    # Finding the most common words in the reference text
    wordFreq = sortWords(refList, 3)
    print("Most Common Words in Wells")
    print(wordFreq[0:5])
    # Finding the most common words in the reference text
    print("Most Common Words in Cipher")
    print(sortWords(cipherList, 3))

    # Comparing letter frequencies of the reference and cipher texts
    print("Most Common Letters in Wells")
    # Checking letter frequency in reference text
    refText = str(refList)
    refTextFreq = letterFrequency(refText)
    refListFreq = list(refTextFreq.items())
    refListFreq.sort(key=getFreq, reverse=True)
    print(refListFreq)

    # Checking letter frequency in reference text.
    print("Most Common Letters in Cipher")
    cipherText = ' '.join(cipherList)
    cipherTextFreq = letterFrequency(cipherText)
    cipherListFreq = list(cipherTextFreq.items())
    cipherListFreq.sort(key=getFreq, reverse=True)
    print(str(cipherListFreq) + "\n")

    # Trying to replace most common in cipher text with most common in Wells
    cipherText = cipherText.replace('y', 'T')
    cipherText = cipherText.replace('b', 'H')
    cipherText = cipherText.replace('m', 'E')
    cipherText = cipherText.replace('r', 'S')
    cipherText = cipherText.replace('a', 'A')
    cipherText = cipherText.replace('t', 'R')
    cipherText = cipherText.replace('x', 'N')
    cipherText = cipherText.replace('h', 'D')
    cipherText = cipherText.replace('i', 'U')
    cipherText = cipherText.replace('s', 'M')
    cipherText = cipherText.replace('p', 'G')
    cipherText = cipherText.replace('g', 'L')
    cipherText = cipherText.replace('c', 'I')
    cipherText = cipherText.replace('v', 'V')
    cipherText = cipherText.replace('w', 'Y')
    cipherText = cipherText.replace('n', 'F')
    cipherText = cipherText.replace('f', 'O')
    cipherText = cipherText.replace('u', 'C')
    cipherText = cipherText.replace('d', 'K')
    cipherText = cipherText.replace('f', 'O')
    cipherText = cipherText.replace('k', 'P')
    cipherText = cipherText.replace('o', 'W')
    cipherText = cipherText.replace('z', 'B')

    # Printing deciphered text
    print(str(cipherText))


decode()
