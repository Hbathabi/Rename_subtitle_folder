import os

#Target folder for name to change
folder = r'Path from Driver\\'

#Target folder for name to get
sorFolder =  r'Path from Driver\\'



#creat new list to save new name for files 
newName =[]


for file_name in os.listdir(sorFolder):
    # Construct new file name with extantion
    sorFolder = folder + file_name[:-3]+"srt"
    newName.append(sorFolder)

c = 0

#change name of old file to new  one by one
for name in os.listdir(folder):
    oldName = folder +name
    newNameX= newName[c]
    os.rename(oldName , newNameX)
    c = c+1

print('All Files Renamed')
