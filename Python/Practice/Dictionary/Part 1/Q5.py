# Loop — Frequency / Counting Problem

# Given a sentence as a string, build a dictionary that counts how many times each word appears in the sentence. Do not use collections.Counter — build the counting dictionary manually using a loop.

sentence = "the quick brown fox jumps over the lazy dog the fox runs"

new_sen = sentence.rsplit()
# print(new_sen)

dic = {}

# 1st way
# for word in new_sen:
#     dic[word] = dic.get(word, 0)+1 

# another way
for word in new_sen:
    if word in dic:
        dic[word]+=1
    else:
        dic[word]=1

print(dic)