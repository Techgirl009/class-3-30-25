#os module helps to perform many events like make, delete, and edit files and folders.
import os
#shutil module offers a number of high level operations on files and collections of files.
import shutil

from_dir = "/Users/sjkoganti/Downloads"
to_dir = "/Users/sjkoganti/Desktop/Downloaded_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == '':
        continue
    if extension in ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "document_files"
        path3 = to_dir + '/' + "document_files" + '/' + file_name
        print("path1", path1)
        print("path3", path3)
        if os.path.exists("path2"):
            print("moving" + file_name + "...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving" + file_name + "...")
            shutil.move(path1, path3)


#line 18, continue statements are used inside loops when program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluates the loops conditions.