# Ivana Zdravevska
# CS 100 2019F Section 039
# HW 06, September 25, 2019

'''The function hasFinalLetter should create and return a list of
all the strings in strList that end with a letter in letters.
'''

def hasFinalLetter(strList, letters):
    showList = []
    for string in strList:
        if string.endswith(letters):
            showList.append(string)
    return showList

#Case 1:
list1 = ['apple', 'orange', 'banana', 'peach', 'juice']
letters1 = 'e','K','B','O'

final1 = hasFinalLetter(list1,letters1)
print(final1)
print(" ")

#Case 2:
list2 = ['desk','pencil','pen','chair','stapler','eraser']
letters2 = 'l','r','P','E','J'

final2 = hasFinalLetter(list2,letters2)
print(final2)
print(" ")

#Case 3:
list3 = ['window','wall','paint','door','couch']
letters3 = 'p','c','D','N','T'

final3 = hasFinalLetter(list3,letters3)
print(final3)
print(" ")

'''The function isDivisible should create and return a list of all the ints
in the range from 1 to maxInt (not including maxInt) that are divisible
of both ints in twoInts
'''

def isDivisible(maxInt,twoInts):
    showValues=[]
    for i in range(maxInt):
        if i%twoInts[0]==0 and i%twoInts[1]==0:
            showValues.append(i)
    return showValues

#Case 1:
int1=100
tuple1=(3,5)
final4 = isDivisible(int1,tuple1)
print(final4)
print(" ")

#Case 2:
int2= 100
tuple2=(2,4)
final5=isDivisible(int2,tuple2)
print(final5)
print(" ")

#Case 3:
int3= 200
tuple3= (6,3)
final6= isDivisible(int3,tuple3)
print(final6)
