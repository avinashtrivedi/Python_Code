print('Enter the first submission:')
x = input()
print('Enter the second submission:')
y = input()

# create dictionary to hold unique words from each submission
my_x_dict={}
my_y_dict={}

# store words in my_x_dict
for i in x.split(' '):
    if i in my_x_dict:
        my_x_dict[i] = my_x_dict[i] + 1
    else:
        my_x_dict[i] = 1

# store words in my_y_dict
for i in y.split(' '):
    if i in my_y_dict:
        my_y_dict[i] = my_y_dict[i] + 1
    else:
        my_y_dict[i] = 1

unique_word = []
common_word = []

# get word in lower case form from my_x_dict
unique_word = [i.lower() for i in my_x_dict.keys()]

# check for each word in my_y_dict
# and store in unique_word if word does not already exist
# else store in common_word

for i in my_y_dict.keys():
    if i.lower() not in unique_word:
        unique_word.append(i.lower())
    else:
        common_word.append(i.lower())

# compute similarity
similarity_score = len(common_word)/len(unique_word)
print('The similarity score between the two is: {}%.'.format(round(similarity_score*100,2)))