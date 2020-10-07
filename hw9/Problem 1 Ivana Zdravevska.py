# Ivana Zdravevska
# CS 100 2019F Section 039
# HW 09, October 24, 2019

#Problem 1 
def file_copy(in_file, out_file):
    in_file2 = open(in_file,'r')
    out_file2 = open(out_file,'w')
    for line in in_file2:
        out_file2.write(line)
    out_file2.close()
    in_file2.close()

'''
Testing the output:

file_copy('sample.txt', 'copy.txt')
copy_f = open('copy.txt')
copy_f.read()
print(copy_f)
'''
