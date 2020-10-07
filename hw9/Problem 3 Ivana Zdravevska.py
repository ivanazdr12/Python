# Ivana Zdravevska
# CS 100 2019F Section 039
# HW 09, October 24, 2019

#Problem 3
def repeat_words(in_file, out_file):
    import string
    inF = open(in_file,'r')
    outF = open(out_file,'w')
    body = inF.readlines()

    for line in body:
        words = line.split()
        duplicates = []
        clean_words=[]
        for word in words:
            result = word.lower().strip(string.punctuation)
            clean_words.append(result)
        for word in clean_words:
            if clean_words.count(word)>1 and word not in duplicates:
                duplicates.append(word)
        if len(duplicates)!=0:
            outF.write(" ".join(duplicates))
            outF.write("\n")
    inF.close()
    outF.close()


'''
Testing the output:

inF = 'catInTheHat.txt'
outF = 'catRepWords.txt'
repeat_words(inF, outF)
'''
