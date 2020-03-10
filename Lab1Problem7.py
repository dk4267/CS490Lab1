from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
import nltk
import string

#open and read file, save one version with and one version without punctuation
inFile = open('nlp_input.txt', 'r')
theText = inFile.read()
text = theText.translate(str.maketrans('', '', string.punctuation))

#tokenize text without punctuation into words
tokens = nltk.word_tokenize(text)

#lemmatize each token, add to a list
lemmatized = []
lemmatizer = WordNetLemmatizer()
for s in tokens:
    lemmatized.append(lemmatizer.lemmatize(s))

#make trigrams from lemmatized words
trigrams = ngrams(lemmatized, 3)

#make dictionary to keep track of the frequency of each trigram
triDict = {}
for s in trigrams:
    if s in triDict:
        triDict.update({s: triDict.get(s) + 1})
    else:
        triDict.update({s: 1})

#put into tuples and sort by value, similar to problem 2 of the lab
triList = []
for key, value in triDict.items():
    triTuple = (value, key)
    triList.append(triTuple)

#find 10 most common trigrams
topTenTris = sorted(triList, reverse=True)[:10]

#turn each trigram tuple from top ten list into a string
finalTris = []
for i in topTenTris:
    triVal = i[1]
    stringTri = triVal[0] + ' ' + triVal[1] + ' ' + triVal[2]
    finalTris.append(stringTri)

#tokenize original text into sentences
#for each sentence token, go through top ten trigram list
#if trigram is in sentence, add sentence to the final result text
result = ''
sentenceTokens = nltk.sent_tokenize(theText)
for s in sentenceTokens:
    for i in finalTris:
        if i in s:
            result += s
            break
print(result)