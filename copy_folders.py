# The intention here is to Copy semi automate some of the copy paste stuff
# 1) Create the Directories needed
# 2) Copy the files needed into newly created directories
# MANUAL WORK DONE HERE, Compare the speadsheets to create new version.
# 3) Change the file names to their appropriate names
# 4) Copy the file names back into needed Directory
# -----------------------------------------------
# 5) Create a function that can read the file names
# 6) Itterate over name change of file see changeFileName function


import os
from shutil import copy
from shutil import rmtree

spreadsheetNames = []

path = "/Users/bastianawischus/Documents/Git/work_automation/"
#path = os.getcwd
# Use above line to work in current directory
def createFolder():
    try:
        for x in spreadsheetNames:
            os.mkdir(path + x)
    except:
        print("An error occured creating the Folder Stucture")

def copyFiles():
    try:
        for x in spreadsheetNames:
            copy(path + "/sourceFiles/TestSheet1.xlsx", path + x)
    except:
        print("An error occured coping the files")

def changeFileName():
    try:
        for x in spreadsheetNames:
            os.rename(path + x + "/TestSheet1.xlsx", path + x + "/NewName1.xlsx")
            # The NewName1 is hardcoded, this will cause all the files be called
            # NewName1 and copied over. Need to figure out how to add indecies 
    except:
        print("An error occured changing file names")

def copyHome():
    # For testing purpose only, instead of creating a HomeFolder we can copy them into a Source File.
    try:
        if os.path.isdir(path + "HomeFolder") == False:
            os.mkdir(path + "HomeFolder")
        for x in spreadsheetNames:
            copy(path + x + "/NewName1.xlsx", path + "HomeFolder")
    except:
        print("An error occured copying the files to the Home directory")

def cleanUpFolders():
    try:
        for x in spreadsheetNames:
            rmtree(path + x)
    except:
        print("An error occured cleaning up the directory structure")

def readFolderNamesFromFile():
    try:
        f=open("spreadsheetNameList.txt", "r")
        f1=f.readlines()
        for x in f1:
            spreadsheetNames.append(x)
        #print(speadsheetNames) # ignore the \n. Reading the index it is not there
    except:
        print("Can not read spreadsheetNameList.txt")

readFolderNamesFromFile()
createFolder()
copyFiles()
changeFileName()
copyHome()
cleanUpFolders()