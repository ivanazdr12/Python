# Ivana Zdravevska
# CS 100 2019F Section 039
# HW 05, September 23, 2019

"""
1. Create a list named months of the months of the year. Write a
for loop that iterates over the elements of months and prints
out each one that begins with letter 'J', one month per line
"""
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October','November','December']
for month in months:
    if month[0] == 'J':
        print(month)
print(" ")



"""
2. Write a for loop that iterates over all of the integers in the range 0
through 99, inclusive, and prints out all of those numbers that are divisible
by both 2 and 5.
"""
for i in range(0,99+1):
    if(i%2==0 and i%5==0):
        print(i)
print(" ")



"""
3. Write a for loop that prints out all the vowels in horton in the order
they appear in horton.
"""
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU" 
for letters in horton:
    if letters in vowels:
        print(letters)
