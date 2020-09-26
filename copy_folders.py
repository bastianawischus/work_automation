# The intention here is to Copy semi automate some of the copy paste stuff
# 1) Create the Directories needed
# 2) Copy the files needed into newly created directories
# MANUAL WORK DONE HERE, Compare the speadsheets to create new version.
# 3) Change the file names to their appropriate names
# 4) Copy the file names back into needed Directory
# -----------------------------------------------

import os
import xlrd
from shutil import copy
from shutil import rmtree

path = "/Users/bastianawischus/Documents/Git/work_automation/"
#path = os.getcwd
def createFolder():
    try:
        #print(os.getcwd)
        #print(path)
        os.mkdir(path + "Folder1")
        os.mkdir(path + "Folder2")
        os.mkdir(path + "Folder3")
        os.mkdir(path + "Folder4")
        os.mkdir(path + "Folder5")
    except:
        print("An error occured creating the Folder Stucture")

def copyFiles():
    try:
        copy(path + "/sourceFiles/TestSheet1.xlsx", path + "Folder1")
        copy(path + "/sourceFiles/TestSheet2.xlsx", path + "Folder2")
        copy(path + "/sourceFiles/TestSheet3.xlsx", path + "Folder3")
        copy(path + "/sourceFiles/TestSheet4.xlsx", path + "Folder4")
        copy(path + "/sourceFiles/TestSheet5.xlsx", path + "Folder5")
    except:
        print("An error occured coping the files")


def changeFileName():
    try:
        os.rename(path + "Folder1/TestSheet1.xlsx", path + "Folder1/NewName1.xlsx")
        os.rename(path + "Folder2/TestSheet2.xlsx", path + "Folder2/NewName2.xlsx")
        os.rename(path + "Folder3/TestSheet3.xlsx", path + "Folder3/NewName3.xlsx")
        os.rename(path + "Folder4/TestSheet4.xlsx", path + "Folder4/NewName4.xlsx")
        os.rename(path + "Folder5/TestSheet5.xlsx", path + "Folder5/NewName5.xlsx")
    except:
        print("An error occured changing file names")

def copyHome():
    # For testing purpose only, instead of creating a HomeFolder we can copy them into a Source File.
    try:
        if os.path.isdir(path + "HomeFolder") == False:
            os.mkdir(path + "HomeFolder")
        copy(path + "Folder1/NewName1.xlsx", path + "HomeFolder")
        copy(path + "Folder2/NewName2.xlsx", path + "HomeFolder")
        copy(path + "Folder3/NewName3.xlsx", path + "HomeFolder")
        copy(path + "Folder4/NewName4.xlsx", path + "HomeFolder")
        copy(path + "Folder5/NewName5.xlsx", path + "HomeFolder")
    except:
        print("An error occured copying the files to the Home directory")

def cleanUpFolders():
    try:
        rmtree(path + "Folder1")
        rmtree(path + "Folder2")
        rmtree(path + "Folder3")
        rmtree(path + "Folder4")
        rmtree(path + "Folder5")
    except:
        print("An error occured cleaning up the directory structure")

createFolder()
copyFiles()
changeFileName()
copyHome()
cleanUpFolders()