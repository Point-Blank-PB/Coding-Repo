import random

#change this string to alter the frequency of the selected alphabets
string = 'aaaaaaaaaaaaaaaabcdeeeeeeeeeeeeeeefghiiiiiiiiiiiiiiiijklmnooooooooooooooopqrstuuuuuuuuuuuuuuvwxyz'
file = open('testcases_weirdo.txt', 'w')
file.write('1\n')

#change this number to alter the no. of strings in the given test case
file.write('9999\n')

for i in range(9999):
    s = ""
    for j in range(2, 20):     #alter this range to change the length of created string 
        s = s + string[random.randint(0, len(string)-1)]
    file.write(s.lower() + '\n')

file.close()
