import jsonlines
import re
g = open("result.txt","w", encoding="utf-8")
def count(st):
    res = 0
    for i in range(len(st)):
        if (i == '@'):
            res +=1
    return res
regex =  re.compile('@\d+')
films = list(open('films.txt').readlines())
i = 0

import io
with open('train_final.txt', encoding="utf-8") as reader:
    for line in reader:
        sentence = ''
        x = re.split("\s", line)
        for word in x:
            print(word)