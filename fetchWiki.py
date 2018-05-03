# Gets the list of all links from wiki and saves in a file
import wikipedia as wiki
import pickle

for type in ["theorems", "lemmas", "inequalities"]:
    theList = wiki.page("list of " + type)
    print('Page loaded.')
    links = theList.links
    print('Links loaded.')

    #clean up array
    cleaned = []
    keyword = ["theorem", "Theorem", "lemma", "Lemma", "inequality","Inequality","inequalities", "Inequalities", "approximation"] # many inequalities are called theorems

    #if type == "theorems":
    #    keyword =  ['theorem', 'Theorem']
    #elif type == "lemmas":
    #    keyword = ["lemma","Lemma"]
    #elif type == "inequalities":
    #    keyword = ["inequality","Inequality","inequalities", "Inequalities", "theorem"] # many inequalities are called theorems

    print ('Type: ' +type+'\n\n')

    for title in links:
        if any(key in title for key in keyword):  #check if any keyword id present inside the title name string, great set theoretic use of python!
            cleaned.append(title)
        else:
            print('Dropping ' + title)

    myFile = open(type + 'List.dat', 'wb')	# Opening in binary foramt
    pickle.dump(cleaned, myFile)
    myFile.close()
    print('File created.')
