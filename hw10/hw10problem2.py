# Ivana Zdravevska
# CS 100 2019F Section 039
# HW 10, October 29, 2019

#Problem 2
def initialLetters(wordList):
    frequency = {} 
    for word in wordList:
        frequency[word[0]] = [word]
    return frequency

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetters(horton))
