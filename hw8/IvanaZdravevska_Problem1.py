# Ivana Zdravevska
# CS 100 2019F Section 039
# HW 08, October 21, 2019

#Problem 1
def twoWords(length,firstLetter):
    word1 = "filler"
    word2 = "filler"
    result = []
    while True:
        word1 = input("Enter a " + str(length) + " letter word: ")
        if length== len(word1):
            break
    while True:
        word2 = input("Enter a word beginning with " + firstLetter + ": ")
        if word2[0]==firstLetter.upper() or word2[0]==firstLetter.lower():
            break
    return [word1,word2]

print(twoWords(4,"B"))  
