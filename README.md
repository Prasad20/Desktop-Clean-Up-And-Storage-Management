# Infra-structure-Assignment

In this program at first you have to specify whether your working on linux or windows then total number of directories you want to Look into(atleast one) and then enter the path of directories you want to look into.

1.Searching for top 10 files(name of the function in code is (function)):-
      In this function first all the file's path in a directory(including subfolders) will be added into a list and then another list will contain the size of files. Then a matrix of path and size will be created and it is sorted according to the size.
      
Now the function ends and the top 10 files or if your directory doesnt files less than 10 then all files will be shown with their size in MB and there path.

Now enter the directory of your desktop: like "C:\Users\PRASAD PARSHALLU\Desktop"

Now enter the Enter the directory where you want to store desktop files: "like C:\Users\PRASAD PARSHALLU\Documents"

Few files with extensions like mp4 are stored in Video folder, png and jpeg are stored in Images folder, txt are stored in text folder and doc are stored WordDocuments folder.
      
2.Moving the files from desktop to documents(name of the function in code is (func)):-
      In this function everything is same as in above function just files in sub-directories, .exe(extension), shortcuts... are exlcuded.
      
Now function ends and then a folder is created in documents. According to the list path then sub-folders are created with the name of the file as extension of file and if folder or any sub folder already exists then new folder is not created. Later, the files are moved according to there extension in respective folders and if file already exisits then the copy of file is just removed from desktop. This is continued untill whole list is traversed. 
