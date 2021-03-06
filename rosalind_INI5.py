# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:22:18 2022

@author: Moogie
"""
# =============================================================================
# Working with Files: 
# To access a file, you must first open it. To do so, you can use the open() function, which takes two parameters: the name of the target file and the mode. Three modes are available:

# r - read mode (the file is opened for reading)
# w - write mode (the file is opened for writing, and if a file having the same name exists, it will be erased)
# a - append mode (the file is opened for appending, which means that data is only to be added to the existing data in the file)
#
# f = open('input.txt', 'r')
# This code told Python to open the file input.txt in r mode and store the result of this operation in a file object called f.
# ----------------------------------------------------------------------------
# To obtain data from the file object you created, you can apply the following methods:

# The command f.read(n) returns n bytes of data from the file as a string. When the size parameter is omitted, the entire contents of the file will be read and returned.

# The command f.readline() takes a single line from the file. Every line (except the last line of file) terminates in a newline character (\n). To remove this character from the end of a line you have read, use the .strip() method. Note that every time you call .readline() it takes the next line in the file.

# The command f.readlines() returns a list containing every line in the file. If you need to obtain a particular line, you can use a list item index, e.g., f.readlines()[2] returns the third line of the file object f (don't forget that Python utilizes 0-based numbering!)
# ----------------------------------------------------------------------------
# An alternative way to read lines is to loop over the file object.

# for line in f:
#   print line
# ----------------------------------------------------------------------------
# If the data in the file are not separated by new lines but rather by whitespace, commas, or any other delimeter, then all three commands above will return the data only in the form of lines. As a workaround, you can use the command line .split(). It uses whitespace in addition to \n as delimeters by default, and runs of the same delimiter are regarded as a single separating space. For example,

# 'Beautiful is better than ugly.\n'.split() returns ['Beautiful', 'is', 'better', 'than', 'ugly.']

# You can even specify the delimiter as a parameter of line.split():

# 'Explicit, is better, than implicit.'.split(",") returns ['Explicit', ' is better', ' than implicit.']

# Another convenient command for file parsing is .splitlines(). It returns a list of the lines in the string, breaking at line boundaries. Line breaks are not included.

# 'Simple is\nbetter than\ncomplex.\n'.splitlines() returns ['Simple is', 'better than', 'complex.']
#-----------------------------------------------------------------------------
# To save a file, output the desired file in write mode (if there is no such file, it will be created automatically):

# f = open('output.txt', 'w')
# You can then write your data using .write() method.

# f.write('Any data you want to write into file')
# The command f.write(string) writes the contents of string to file f. If you want to write something other than a string (an integer say), you must first convert it to a string by using the function str().

# inscription = ['Rosalind Elsie Franklin ', 1920, 1958]
# s = str(inscription)
# f.write(s)
# You also can write list items into a file one at a time by using a for loop:

# for i in inscription:
  # f.write(str(i) + '\n')
# Adding \n to str(i) means that every item will start with a new line.

# When you are finished writing file, don't forget that you must close it using the command f.close(). It's a good habit to get into.

# =============================================================================

# =============================================================================
# Problem
# Given: A file containing at most 1000 lines.
# 
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
# 
# Sample Dataset
# Bravely bold Sir Robin rode forth from Camelot
# Yes, brave Sir Robin turned about
# He was not afraid to die, O brave Sir Robin
# And gallantly he chickened out
# He was not at all afraid to be killed in nasty ways
# Bravely talking to his feet
# Brave, brave, brave, brave Sir Robin
# He beat a very brave retreat
#
# Sample Output
# Yes, brave Sir Robin turned about
# And gallantly he chickened out
# Bravely talking to his feet
# He beat a very brave retreat
# =============================================================================

f = open('rosalind_ini5.txt', 'r')
# print(f.readlines())
# tried to do count/indexing with i, didn't work. Too much int vs string, out of range, etc. Too complicated anyway.
new_lines = []

for line in f.readlines():
    
    new_lines.append(str(line.strip('\n')))
    # line.splitlines() did NOT work. Added double quotes " " to random(?) lines from the txt file.

f = open('rosalind_ini5_output.txt', 'w')

for line in new_lines:
    if new_lines.index(line) % 2 == 1:
        f.write(str(line.strip("'[]'")+'\n'))
        # f.write(str(line)+'\n')

f.close()
# with open('D:/Programming/Python/Marianne_doodie/rosalind_datasets/rosalind_ini5.txt', 'r') as f:
     # lines = f.readlines() 

# Answer/Explanation:
# f = open('rosalind_ini5.txt', 'r')
# g = open('output.txt', 'w') 
# for x in f.readlines()[1::2]: 
#     g.write(x) 
# g.close()




