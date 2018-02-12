import os
import sys
import platform

a = []                                                          # stores the path and size of file in 2d matrix format

seperator = ""                                                  # As seperator in windows and other os are different

def search_in_directory(path):
    pList = []                                                   #pList will store the path of file
    for dirpath, subdirs, files in os.walk(path):               # for loop to search files in sub-folders
        for x in files:
            pList.append(os.path.join(dirpath, x))

    sList = []                                                  #slist[] will store the size of file
    for file in pList:                                           # for loop to store size of files in List "pList"
        sList.append(os.stat(file).st_size)

    for i in range(len(pList)):                                  # for loop to append path and size of file in list "a"
        a.append([pList[i], sList[i]])

    a.sort(key=lambda x: x[1])                                   # sort the List "a" w.r.t size

def files_in_directory(directory):
    pList = []                                                   # pList will store the path of file
    for file in os.listdir(directory):                          # for loop to search files in directory
        filename = os.fsdecode(file)
        if not (filename.endswith(".exe") or filename.endswith(".lnk") or os.path.isdir(directory + "/" + file)):
            pList.append(os.path.join(directory, filename))

    slist = []                                                   #slist[] will store the size of file
    for file in pList:                                            # for loop to store size of files in List "pList"
        slist.append(os.stat(file).st_size)

    for i in range(len(pList)):                                    # for loop to append path and size of file in list "a"
        a.append([pList[i], slist[i]])


# Program starts from here

if (platform.system() == "Windows"):                              # As for windows directories has "\" as seperator and for linux it is "/" this is done by the following if
    seperator = '\\'
else:
    seperator = '/'

s = input("Enter number of Directories you want to search into: ")                        # s is a dummy variable just to store number of directories you want to search

l = []                                                                  # l is a list storing the directories you want to search into

for i in range(int(s)):                                                 # append the directories you want to search into
    k = input("Enter the Directory:")
    l.append(k)

for i in range(int(s)):                                                 # for loop will call function to search in directory for all directories you want entered before
    search_in_directory(l[i])                                           # this function will store all the files path and size in the given directory and in its sub-folders in list a

for x in (range(10) or (range(len(a)))):                                # Print 10 largest files in the directory or if files are less than 10 then print them all with their size in MB
    print('[%s]'"MB "'[%s]' % (a[-1 - x][1] / 1000000, a[-1 - x][0]))

a.clear()                                                               # Remove all the directories that you appended to search 10 largest files

path = input("Enter your desktop directory or any other directory in which you want to sort the files into a folder :")    # path will store the directory in which you want to move the files in a folder

newpath = input("Enter the directory where you want to move the files :")    # newpath will be store the directory where the files are to be moved

files_in_directory(path)                                               # this function store all the_files_path and size in the_directory in list "a"

newpath+= seperator + "desktop"                                     # the newpath add folder name called ("desktop") to its path

if not os.path.exists(newpath):                                     # if desktop folder doesnt exists then desktop directory will be created
    os.makedirs(newpath)

for x in range(len(a)):                                              #this for loop will search all the files appended in list "a"
    old = a[-1 - x][0]                                               # old will store the path of the file
    temp = old.split(seperator)                                      # temp will store the file name with the extension
    temp = (temp[len(temp) - 1])

    filen = temp.split(".")                                          # filen will store the file name with extension
    foldn = (filen[len(filen) - 1])                                  # foldn will store the extension of the file

    if (foldn == "mp4"):
        foldn = ""
        foldn = "Vedio"
    elif foldn == "png" or foldn == "jpeg":
        foldn = ""
        foldn = "Images"
    elif (foldn == "txt"):
        foldn = ""
        foldn = "texts"
    elif (foldn == "doc"):
        foldn = ""
        foldn = "WordDocuments"

    newpath1 = newpath + seperator + foldn                            #newpath1 will create the path of sub-folder of desktop folder

    if not os.path.exists(newpath1):                                  #if sub-folder already exists then no folder is created
        os.makedirs(newpath1)

    tfilen = ""
    tfilen = str(newpath1) + seperator + str(temp)                  #tfilen will create the path of file to be moved in the sub folder

    if not os.path.exists(tfilen):                                 #if the file exists already in the subfolder then file is not copied again in the sub-folder
        os.rename(old, tfilen)
    else:
        os.remove(old)                                             #the file in the driectory is removed

print("Your files are successfully moved in the folder called desktop")

sys.exit()
