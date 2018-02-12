# Infra-structure-Assignment

In this program at first you have to specify the total number of directories you want to look into(atleast one) and then enter the path of directories you want to look into.

1.Searching for top 10 files(name of the function in code is (search_in_directory)):-
      In this function first all the file's path in a directory(including subfolders) will be added into a list and then another list will contain the size of files. Then a matrix of path and size will be created and it is sorted according to the size.
      
Now the function ends and the top 10 largest files or if your directory have less than 10 files then all files will be shown with their size in MB and there path.

Now enter the directory of your desktop or any other directory in which you want to sort the files into a folder: like "C:\Users\PRASAD PARSHALLU\Desktop"

Now enter the directory where you want to move files : "like C:\Users\PRASAD PARSHALLU\Documents"

Few files with extensions like mp4 are stored in Video folder, png and jpeg are stored in Images folder, txt are stored in text folder and doc are stored WordDocuments folder.
      
2.Moving the files from desktop to documents(name of the function in code is (files_in_directory)):-
      In this function everything is same as in above function just files in sub-directories, .exe(extension), shortcuts... are exlcuded.
      
Now function ends and then a folder is created in specified directory(like Documents). According to the extension of files then sub-folders are created with the name of the file as extension of file and if folder or any sub folder already exists then new folder is not created. Later, the files are moved according to there extension in respective folders and if file already exisits then the copy of file is just removed from given directory(like Desktop). This is continued untill all files are traversed in that directory(like Desktop). 

For example code runs in this manner:-

Enter number of Directories you want to search into:2
Enter the Directory: C:\Users\PRASAD PARSHALLU\Desktop
Enter the Directory: C:\Users\PRASAD PARSHALLU\Download

All the 10 largest files or if your directory have less than 10 files then all files will be shown with their size in MB and there path.

Enter your desktop directory or any other directory in which you want to sort the files into a folder : C:\Users\PRASAD PARSHALLU\Desktop
Enter the directory where you want to move the files :C:\Users\PRASAD PARSHALLU\Documents

Now a folder called desktop is created in the documents directory and sub-folders are created in desktop folder according to the files extension and if any sub-folder or desktop folder already exists then no new folder is created instead same folder will contain all the moved files from desktop. As the file is transferred into subfolder in desktop folder in documents directory this file will be deleted from desktop directory.

Your files are successfully moved in the folder called desktop is printed

and program ends.
