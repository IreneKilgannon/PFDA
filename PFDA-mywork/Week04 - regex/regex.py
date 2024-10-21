# Code from lab

import re 
 
regex = "wwww\.\.+\.com"
filename = 'access.log'
 
with open(filename) as inputFile: 
    for line in inputFile: 
        foundTextList = re.findall(regex, line)
        print(foundTextList)
        #if (len(foundTextList)!= 0): 
        #    print(foundTextList) 
            #foundText = foundTextList[0] 
            #print(foundText) 
            # if I did not want the [] at the beginning and end 
            #print(foundText[1:-1]) 
 
 
#regex = 'wwww[a-zA-Z]\.com'

 
#regex = "wwww\.\.+\.com" to find the url's in the file