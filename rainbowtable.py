# import the library
import hashlib
import sys

# try-except block to handle the exception
try:
    # command line argument
    filename = sys.argv[1]
except:
    print('Please enter proper filename.')
    sys.exit()

# create md5 hashing object
hashobj = hashlib.new(name='md5')

# Password Hash Dictionary
PasswordHashDictionary = {}

try:
    
    # read the password line by line
    with open(filename) as file:

        # skip first 11 line ,as it contains comment only.
        for _ in range(11):
            next(file)

        # process the password after line 11
        while (passwd := file.readline()):

            # remove leading and trailing whitespace
            passwd = passwd.strip()

            # Encode the string
            passwd_encoded = passwd.encode(encoding='utf_16_le')

            # Update the hash object's state
            hashobj.update(passwd_encoded)

            # add password and hash in dictionary
            PasswordHashDictionary[hashobj.hexdigest()] = passwd
except:
    print('file does not exist.')
# sort the dictionary on the basis of key i.e. Hash
sorted_dict = dict(sorted(PasswordHashDictionary.items(),key=lambda x:x[0]))

# print
for k,v in sorted_dict.items():
    print('[{}]:[{}]'.format(k,v))