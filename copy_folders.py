# The intention here is to Copy semi automate some of the copy paste stuff
# 1) Create the Directories needed
# 2) Copy the files needed into newly created directories
# MANUAL WORK DONE HERE, Compare the speadsheets to create new version.
# 3) Change the file names to their appropriate names
# 4) Copy the file names back into needed Directory
# -----------------------------------------------
# NOTE: 
# - The Directory structure needs to be updated to template structure. Its likely to remain static. 
# - Not all these opperations need to happend in an instance. Implement passing prameter into these to execute the funtions.
# - This is not fully automation as between S2 and S3 manual labor needs to get done. If this gets automated in the future then just call the sript in a updateTemplate function.
# - This is a fast build prototype / proof of concept. I know how bad it is to have everything hard coded.
# - I belive this does not work if the files or folders currently exist. Need to encapusate all logic in try catch.

# - Keep in mind when Adding speadsheet, get the names from a file, Speadsheet name -> Conversion Name.
# - Speadsheet name changes

import os
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