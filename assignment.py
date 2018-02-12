import os
import sys

a = []

seperator = ""

def function(path):
    List = []
    for dirpath, subdirs, files in os.walk(path):
        for x in files:
            List.append(os.path.join(dirpath, x))

    nlist = []
    for file in List:
        nlist.append(os.stat(file).st_size)

    for i in range(len(List)):
        a.append([List[i], nlist[i]])

    a.sort(key=lambda x: x[1])


def func(directory):
    List = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if not (filename.endswith(".exe") or filename.endswith(".lnk") or os.path.isdir(directory + "/" + file)):
            List.append(os.path.join(directory, filename))

    nlist = []
    for file in List:
        nlist.append(os.stat(file).st_size)

    for i in range(len(List)):
        a.append([List[i], nlist[i]])
def setSep(w):
    global seperator
    if w == '1':
        seperator = '\\'
        print(seperator)
    else:
        seperator = '/'

w = input("Enter 1 for windows and 2 for Linux")

setSep(w)


s = input("Enter number of Directories you want to look into: ")

l = []
for i in range(int(s)):
    k = input("Enter the Directory:")
    l.append(k)

for i in range(int(s)):
    function(l[i])

for x in range(10):
    print('[%s]'"MB "'[%s]' % (a[-1 - x][1] / 1000000, a[-1 - x][0]))

a.clear()

p = input("Enter your desktop directory ")

s = input("Enter the directory where you want to store desktop files :")

func(p)

newpath = s + seperator + "desktop"

if not os.path.exists(newpath):
    os.makedirs(newpath)

for x in range(len(a)):
    old = a[-1 - x][0]
    temp = old.split(seperator)
    temp = (temp[len(temp) - 1])

    filen = old
    filen += seperator + temp

    filen = temp.split(".")
    foldn = (filen[len(filen) - 1])

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

    newpath1 = newpath
    newpath1 += seperator + foldn

    if not os.path.exists(newpath1):
        os.makedirs(newpath1)

    tfilen = ""
    tfilen = str(newpath1) + seperator + str(temp)

    if not os.path.exists(tfilen):
        os.rename(old, tfilen)
    else:
        os.remove(old)
