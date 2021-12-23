def round_history(filepath):
    """
    >>> round_history('files/game1.txt')
    >>> with open('files/game1_fixed.txt', 'r') as outfile1:
    ...     print(outfile1.read().strip())
    W
    L
    L
    >>> round_history('files/game2.txt')
    >>> with open('files/game2_fixed.txt', 'r') as outfile2:
    ...     print(outfile2.read().strip())
    L
    L
    W
    L
    L
    W
    L
    L
    W
    """
    with open(filepath, 'r') as inputfile:
        data = inputfile.readlines()
        
    outfile = filepath.split('.txt')[0]+'_fixed.txt'
    f = open(outfile,'w')
    newline = ''
    for i in data:
        row = i.split(',')
        f.write(newline)

        if row[0]=='Attackers':
            f.write('W')
        else:
            f.write('L')
        newline = "\n"
    f.close()