# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import shutil

test_pth = "test"


def new_jar():
    if not os.path.exists(test_pth):
        os.makedirs(test_pth)
        for file in os.listdir():
            # file_path = os.path.join( file)
            if file.endswith('.jar'):
                shutil.copy(file, test_pth)
    os.chdir(test_pth)
    for file in os.listdir():
        # file_path = os.path.join( file)
        print(file)
        os.system('jar -xvf '+file)
    os.system('del  *.jar')
    os.system('jar -cvfM out.jar . ')


# if (os.path.exists(test_pth)):
#     os.remove(test_pth)
# os.makedirs(test_pth)
new_jar()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
