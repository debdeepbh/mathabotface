import wikipedia as wiki
from random import randint
# Option 1: Downloaded https://github.com/daxeel/TinyURL-Python
# change urllib2 to urllib3 in the tinyurl.py file and install using # python3 setup.py install
# Didn't work
#import tinyurl
# Option 2: Download https://github.com/IzunaDevs/TinyURL 
# Edit the file setup.py and remove the line packages=['TinyURL']
# install fails: Install using sudo python3 setup.py install
# Didn't work
# Option 3: worked; Copy the file TinyURL.py file from IzunaDevs's git to working directory
# so copy the directory to the working directory
import TinyURL as tinyurl

# pickle can dump a list to a file, and load
import pickle
# sys lets you use argv
import sys

allowedTypes = ['theorems','lemmas','inequalities' ]

if len(sys.argv) == 1:
    randomType = randint(0,2)
    # debug here
    #randomType = 0
    print ('No type specified. Assuming random type:', allowedTypes[randomType])
    fileName = allowedTypes[randomType]+'List.dat'
elif sys.argv[1] not in allowedTypes: 
    print ('Usage: python filename.py [theorems | lemmas | inequalities ]')
    exit(1)
else:
    fileName=sys.argv[1]+'List.dat' # e.g. theoremsList.dat

links = pickle.load(open(fileName,'rb'))  # Need to open in binary to read unicode

randomNumber =randint(0,len(links)-1)

# debug here
#randomNumber = 51
print (randomNumber)
randomTitle = links[randomNumber] # Random title
print (randomTitle)

# Get summary of the randomTitle for first 150 chars
articleSummary = wiki.summary(title = randomTitle, sentences=2)


#articleSummary = wiki.summary(title = randomTitle)
articleLink = wiki.page(randomTitle).url

# produce the tinyurl
#tinyLink = tinyurl.shorten(articleLink,"")
tinyLink = tinyurl.create_one(articleLink)
tinierLink = tinyLink.split('//')[1]    #break the string at // and use the second part, which is indexed as [1]
#print (tinyLink)
#print (tinierLink)

#num = 140 - len(tinierLink) - 7 # This number seems optimum based on the behaviour of twitter
num = 280 - len(tinierLink) - 5 # This number seems optimum based on the behaviour of twitter
#num = 280 - len(tinierLink) - 7 # This number seems optimum based on the behaviour of twitter
#num = 280 - 7 # This number seems optimum based on the behaviour of twitter

body = articleSummary[:num]
#print('Summary: ' + body)


if body.partition(' ')[0] == "In":
        firstChunk = body.partition(',')[0]     # the part before comma
        #pprint ( 'FirstChunk: ' +firstChunk)
        removeIn = firstChunk.split(' ',1)[1]   # remove "In"
        hashTag = '#' + removeIn.title().replace(' ','')    # title() makes the first letter of every work upper case, and replace(' ','') removes whitespaces
        gain = len(firstChunk) - len(hashTag) + 1   # gained some letters in this process
        newNum = num + gain
        secondPart = articleSummary[:newNum].partition(',')[2]
        body = hashTag + secondPart # [1]th array element is the ',' itself! That's why [2].

finalString = body + "\n" + tinierLink
#finalString = body + "..\n" + tinierLink
#finalString = body + "\n" #+ tinierLink

print ('Final: ' + finalString)
print (len(finalString))

import sys
from twython import Twython
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

# getting the first image of the file 
#import urllib
#if (len(wiki.page(randomTitle).images) != 0):
#    firstimg = wiki.page(randomTitle).images[0]
#    print ('linkimg:' + firstimg)
#    urllib.request.urlretrieve(firstimg, 'img.jpg')
#    # not sure if image without extension works
#    photo = open('img.jpg', 'rb')
#    response = api.upload_media(media=photo)
#    api.update_status(status=finalString, media_ids=[response['media_id']])
#else:
#   api.update_status(status=finalString)
api.update_status(status=finalString)
