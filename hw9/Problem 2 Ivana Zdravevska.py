# Ivana Zdravevska
# CS 100 2019F Section 039
# HW 09, October 24, 2019

#Problem 2
def file_stats(in_file):
    lines = words = chars = 0
    with open(in_file, 'r', encoding="utf-8") as fd:
        for line in fd:
            lines += 1
            words += len(line.split())  
            chars += len(line)  

    print("lines {0}".format(lines))
    print("words {0}".format(words))
    print("characters {0}".format(chars))

'''
Testing the output:

file_stats('sample.txt')
'''
