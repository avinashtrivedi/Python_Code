
# create a dictionary to store letter and its count.
mydict = {}
for i in set(text):
    if i!=' ':
        mydict[i] = text.count(i)

# sort the dictionary on the basis of count
# and get the most frequent letter
most_frequent = sorted(mydict.items(), key=lambda x: x[1],reverse=True)[0][0]
print(most_frequent)
