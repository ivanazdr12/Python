# Ivana Zdravevska
# CS 100 2019F Section 039
# HW 10, October 29, 2019

#Problem 3
def shareALetter(wordList):
  matches = {}
  for word in wordList:
    if word not in matches:
      matches[word]=[]
      for other_word in wordList:
        for letter in word:
          if letter in other_word and other_word not in matches[word]:
            matches[word].append(other_word)
  return matches
            
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(shareALetter(horton))
