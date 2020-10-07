# Ivana Zdravevska
# CS 100 2019F Section 039
# HW 10, October 29, 2019

#Problem 1
def initialLetterCount(wordList):
    frequency = {} 
    for items in wordList: 
        frequency[items[0]] = wordList.count(items)     
    for key, value in frequency.items(): 
        return frequency

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))
