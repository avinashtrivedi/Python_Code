import os, sys, time

# checking for valid directory name, file size

try:
    folder=sys.argv[1]
    filesize=int(sys.argv[2])
    
except IndexError:
    print("please specify the folder name and file size in KB")
    sys.exit()
except ValueError:
    print('Give number for the file size')
    sys.exit()

#opening the file

f=open('results.txt','w')

print('\nFiles greater than %d KB are\n' % filesize)

# looping through every file, directory in the current directory

for root,dirs,files in os.walk(folder):

# for every file in the directories

    for file in files:

# getting the path of the file

        path=os.path.join(root,file)

# getting the file size

        size=os.path.getsize(path)/1024

# getting the creation time

        seconds=os.path.getctime(path)

# checking for file size and printing and writing to the file

        if size > filesize:

            print("File name: ",file)


            f.write("File name: "+file+'\n')


            print('File Size: %.2f KB'% size)


            f.write('File Size: %.2f KB'% size+'\n')


            print('Creation Date: ',time.strftime("%d %B %Y", time.localtime(seconds)))


            date='Creation Date: ',time.strftime("%d %B %Y", time.localtime(seconds))


            f.write(str(date[0])+str(date[1])+'\n')


            f.write('\n')


            print()

#closing the file

f.close()

