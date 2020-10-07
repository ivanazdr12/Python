# Ivana Zdravevska
# CS 100 2019F Section 039
# HW 08, October 21, 2019

#Problem 3
def enterNewPassword():
    while True:
        password = input('Enter password: ')
        if len(password)<8 or len(password)>15 == False:
            print("The password must be between 8-15 characters long")
            continue
        if any(char.isdigit() for char in password) == False:
            print("The password must have a digit")
            continue
        else:
            print('Password is valid.')
            break
print(enterNewPassword())
