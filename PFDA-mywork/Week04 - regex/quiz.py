# this is code for for the quiz
import re

regex = "^$"
filename = 'quiz.txt'

with open(filename) as quizFile:
    for line in quizFile:
        searchResult = re.search(regex, line)
        if (searchResult):
            matchingLine = line
            # I set the end to blank because each line will already have a \n
            print (matchingLine, end="")

# What line will be printed for the following regular expressions?

#regex = hello, Line 1
# a. hello, Line 1
# b. Hello, Line 3 also lines 2 and 5.
# c. ^Hello, Lines 2, 3
# d. ^Hell*o, Lines 2, 3, 4, 5 and 6 
# e. ^Hell+o, Lines 3 and 6, also line 2
# f. ^Hell?o, Lines 2, 3, 4
# g. ^hello [A-Z], no line
# h. ^Hello [A-Z], line 3
# i. = , line 7
# j. #, line 8
# k.  [, no line, raises an error
# l. ^$, line 10
