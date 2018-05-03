import wikipedia as wiki
from random import randint
# pickle can dump a list to a file, and load
import pickle
# sys lets you use argv
import sys

allowedTypes = ['theorems','lemmas','inequalities' ]

num = 300

if len(sys.argv) == 1:
    randomType = randint(0,2)
    #print ('No type specified. Assuming random type:', allowedTypes[randomType])
    fileName = allowedTypes[randomType]+'List.dat'
elif sys.argv[1] not in allowedTypes: 
    print ('Usage: python filename.py [theorems | lemmas | inequalities ]')
    exit(1)
else:
    fileName=sys.argv[1]+'List.dat' # e.g. theoremsList.dat

links = pickle.load(open(fileName,'rb'))  # Need to open in binary to read unicode
randomNumber =randint(0,len(links)-1)
#print (randomNumber)
randomTitle = links[randomNumber] # Random title
print (randomTitle)
# Get summary of the randomTitle 
articleSummary = wiki.summary(title = randomTitle, sentences=1)
#articleSummary = wiki.summary(title = randomTitle)
articleLink = wiki.page(randomTitle).url
body = articleSummary[:num]

if len(wiki.page(randomTitle).images) != 0:
    firstimg = wiki.page(randomTitle).images[0]
else:
    firstimg = ''

print (randomTitle.title() + ": " +  body + '...' + '\n' + firstimg)
print (articleLink)
