import os
import shutil
def file_organiser():
    try:
        path=input("Enter Source path: ")
        destination=input("Enter destination Path: ")


        list_of_file=os.listdir(path)
        for file in list_of_file:
            name,extension=os.path.splitext(file)
            extension=extension[1:]
            if os.path.exists(destination+'/'+extension):
                shutil.move(path+'/'+file,destination+'/'+extension+'/'+file)

            else:
                os.mkdir(destination+'/'+extension)
                shutil.move(path+'/'+file,destination+'/'+extension+'/'+file)
    except FileNotFoundError:
        print('Source or destination directory does not exist.')
    except PermissionError:
        print('Permission denied. Unable to access files or create folders.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')


file_organiser()