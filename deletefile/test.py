import jsonlines
import re

g = open("result.txt","w", encoding="utf-8")
regex =  re.compile('\d\d\d\d\d\d')
films = list(open('films.txt').readlines())
i = 0
with open('train_final.txt', encoding="utf-8") as reader:
    for line in reader:
        sentence = []
        x = re.split("\s", line)
        for word in x:
            if re.match(regex, word):
                word = '@'+word
                i+=1
            sentence.append(word)
        st = ' '.join(sentence)
        g.write(st)
        g.write('\n')   
g.close()