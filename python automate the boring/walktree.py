import os
#walking through a directory
for folderName, subFolderName, fileNames in os.walk('..'):
    print('The folder is: ' + folderName )
    print('The sub folders in '+ folderName +' are: '+str(subFolderName))
    print('The files in '+ folderName +' are: '+str(fileNames))
    print()
