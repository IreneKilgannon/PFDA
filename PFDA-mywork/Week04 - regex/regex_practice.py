import re

#text = """101 COM    Computers
#205 MAT   Mathematics
#189 ENG   English"""
#pattern = r'\s+'

#re.split(pattern, text)
#print(text)

# Print data on same line
#print(re.sub('\s+', ' ', text))

# Keep data on own line
#print(re.sub('((?!\n)\s+)', ' ', text))



# https://www.machinelearningplus.com/python/python-regex-tutorial-examples/

# Extract the user id, domain name and suffix from the following email addresses:
emails = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""

#desired_output = [('zuck26', 'facebook', 'com'),
# ('page33', 'google', 'com'),
# ('jeff42', 'amazon', 'com')]

pattern = r"(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})"

print(re.findall(pattern, emails, flags= re.IGNORECASE))

# Retrieve all the words starting with 'b' or 'B'
butter = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."""

print(re.findall(r'[Bb]\w+', butter))

# Split the following sentence into words
sentence = """A, very   very; irregular_sentence"""

print(' '.join(re.split(r'[,;\s]+', sentence)))

# Clean up the tweet, remove punctuation,@, #, url's
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

def clean_tweet(tweet):
    tweet = re.sub('http\S+\s*', '', tweet)  # remove URLs
    tweet = re.sub('RT|cc', '', tweet)  # remove RT and cc
    tweet = re.sub('#\S+', '', tweet)  # remove hashtags
    tweet = re.sub('@\S+', '', tweet)  # remove mentions
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)  # remove punctuations
    tweet = re.sub('\s+', ' ', tweet)  # remove extra whitespace
    return tweet

print(clean_tweet(tweet))

# Extract all the text portions between the tags

import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
#print(r.text)  # html text is contained here 

print(re.findall('<.*?>(.*)</.*?>', r.text))