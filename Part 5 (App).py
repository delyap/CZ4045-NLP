import re
import csv

dataset = r'C:/Users/user/Desktop/RPI Overflow Threads.csv'
negationexp = ['no','not','never','none','nobody']
negation = re.compile(r'\b(?:%s)\b' %'|'.join(negationexp))


with open(dataset, encoding='utf8') as source:
    header= True
    csv_data = csv.reader(source,  delimiter=',')
    sentence_count = 0
    for row in csv_data:   
        if header:
            i = 0
            index = 0
            header = False
            for row_header in row:
                if row_header == 'Title':
                    index = i
                i+=1
            continue
        #detect if there is a negation expression and print the sentence
        sentence = row[index]
        if negation.search(sentence):
            print(sentence)
            sentence_count += 1

print(str(sentence_count) + " sentences detected")

