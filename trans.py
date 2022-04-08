

import jsonlines
f = open("or_train.txt", "w", encoding="utf-8")

# with jsonlines.open('test.jsonl', "r", encoding="utf-8") as reader:
#     #for line in reader.iter():
#     for line in reader:
#         for text in (line['messages']):

#             f.write(text['text'])
#             f.write('\n')

# f.close()

####
import io
with jsonlines.open('train_data.jsonl') as reader:
    for line in reader.iter():
        for text in (line['messages']):
            sentence = text['text'].encode('utf-8')
            f.write(text['text'])
            f.write('\n')

f.close()
    