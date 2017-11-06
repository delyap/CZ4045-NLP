from nltk.tokenize import *
import pandas as pd
import re
from sklearn.metrics import precision_recall_fscore_support
import os

script_path = os.path.dirname(os.path.realpath(__file__))
with open( os.path.join(script_path,"tokenizer_input.txt") ,'r') as f:
    data = f.readlines()
data = [x.strip() for x in data] 

y_true = []
y_pred = []
nltk_count = 0
regex_count = 0

regex = r"[\w']+|[.,!?;]"
for s in data:
    nltk_tokens = word_tokenize(s)
    regex_tokens = re.findall(regex, s)
    if len(regex_tokens) > len(nltk_tokens):
        for i in range(len(regex_tokens)-len(nltk_tokens)):
            nltk_tokens.append('')
    elif len(nltk_tokens) > len(regex_tokens):
        for i in range(len(nltk_tokens)-len(regex_tokens)):
            regex_tokens.append('')
    for nltk_token in nltk_tokens:
        y_true.append(nltk_token)
    for regex_token in regex_tokens:
        y_pred.append(regex_token)

#print all tokens by tokenizer
print(y_pred)
#metrics for evaluation
print(precision_recall_fscore_support(y_true, y_pred, average='macro'))
print(precision_recall_fscore_support(y_true, y_pred, average='micro'))
print(precision_recall_fscore_support(y_true, y_pred, average='weighted'))
