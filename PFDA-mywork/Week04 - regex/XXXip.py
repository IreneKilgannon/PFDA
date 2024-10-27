# Write some code that will anonymise the subsomains of ip addresses by X'ing out the last two triplets
# The new lines should be stored in another file

import re


with open('access.log') as inputFile:
    with open('anon_ip.txt', 'w') as outputFile:
        for line in inputFile:
            anon_ip = re.sub(r"(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3} ", "\\1XXX.XXX ", line)
            outputFile.write(anon_ip)

