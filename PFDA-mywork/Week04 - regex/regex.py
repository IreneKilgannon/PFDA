# Code from lab

import re 
 
regex = "wwww\.\.+\.com"

with open('access.log') as inputFile:
    for line in inputFile:
        print(re.findall(r'\[.+\]', line))

        #if     (len(foundTextList)!= 0): 
        #    print(foundTextList) 
            #foundText = foundTextList[0] 
            #print(foundText) 
            # if I did not want the [] at the beginning and end 
            #print(foundText[1:-1]) 
 
 
#regex = 'wwww[a-zA-Z]\.com'

 
#regex = "wwww\.\.+\.com" to find the url's in the file