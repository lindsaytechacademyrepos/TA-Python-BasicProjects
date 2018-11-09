import os
import tkinter
import time


"""
For this drill, you will need to write a script that will check a specific folder on the hard drive, verify whether those files end with a “.txt” file extension and
if they do, print those qualifying file names and their corresponding modified time-stamps to the console.
"""


directory = 'C:\\Users\\linma\\source\\repos\\Tech Academy\\Python-BasicProjects\\filepathDrillFolder'

directoryFiles=os.listdir(directory)

for file in directoryFiles:
    absPath=os.path.join(directory,file) #concatenate directory path and file name into absolute path
    splitText=os.path.splitext(absPath)#get file (root, extension)
    extension=splitText[1] #returns the second entry from splitText (the extension)
    timeModified=time.gmtime(os.path.getmtime(absPath))#gets time modified in seconds since epoch, then converts that into a stuct_time in GMT
    desiredFormat='%m-%d-%y %I:%M:%S' #define the format I want time printed in
    dateTime = time.strftime(desiredFormat,timeModified) #pass in desired format + struct_time, returns dateTime object in human readable format
    if extension == '.txt': #finds files whose extensions are .txt
        print('file %s was modified at %s GMT' %(file,dateTime)) #prints file name and dateTime it was modified

