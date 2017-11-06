import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import ne_chunk, pos_tag

text = "Which distributors are authorized to sell device units?"


sents = sent_tokenize(text)

sentz = word_tokenize(text)  #return tokenized copy of text


print(nltk.pos_tag(sentz))




























##def entities(text):
##    return ne_chunk(
##        pos_tag(
##            word_tokenize(text)))



##tree = entities("When asked about comment, Obama blah blaj blak")
##tree.pprint()
##tree.draw()

##print("\nTEXT: " , text)
##
##print("\n\nSENT_TOKENIZE:" , sents)
##
##print("\n\nWORD_TOKENIZE:" , sentz)
##
##print("\n\n")
##
##print(nltk.wordpunct_tokenize(text))
##
##print("\n\n")
