import os
import shutil
def file_organiser():
    path=r'D:\unorganised files'
    list_of_file=os.listdir(path)
    for file in list_of_file:
        name,extension=os.path.splitext(file)
        extension=extension[1:]
        if os.path.exists(path+'/'+extension):
            shutil.move(path+'/'+file,path+'/'+extension+'/'+file)

        else:
            os.mkdir(path+'/'+extension)
            shutil.move(path+'/'+file,path+'/'+extension+'/'+file)

file_organiser()