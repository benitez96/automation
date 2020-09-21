import os
#Como caminar a traves de un directorio
for folderName, subFolderName, fileNames in os.walk('C:\\delicious'):
    print('The folder is: ' + folderName )
    print('The sub folders in '+ folderName +' are: '+str(subFolderName))
    print('The files in '+ folderName +' are: '+str(fileNames))
    print()
