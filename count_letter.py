
# replce newline with space
lst_poem = poem.replace("\n",' ')

# split the poem using space as separator
lst_poem = lst_poem.split(' ')
total= 0 

# count the words starts with a given letter
for i in lst_poem:
    if i.startswith(letter.lower()) or i.startswith(letter.upper()):
        total = total + 1
