# Ivana Zdravevska
# CS 100 2019F Section 039
# HW 08, October 21, 2019

#Problem 2
def twoWordsV2(length,firstLetter):
    first_input = "filler"
    second_input= "filler"  
    condition = True
    first_input = input("Enter a " + str(length) + " letter word: ")
    while (condition == True): 
        if length == len(first_input):
          condition = False
        else : 
          first_input = input("Enter a " + str(length) + " letter word: ")   
          
    while (condition == False): 
        second_input = input("Enter a word beginning with " + firstLetter+ ":")
        if second_input[0] == firstLetter.upper() or second_input[0] == firstLetter.lower():
          condition = True
    return [first_input,second_input]
print(twoWordsV2(4,'B'))
