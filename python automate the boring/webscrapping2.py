import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code) #->Everything went ok
print(len(res.text)) #->Lenght of what the page had
print(res.text[:30])

print(res.raise_for_status())       #this method will raise an exception if download failed.

playFile = open('RomeoAndJuliet.txt', 'wb') #open/create(?) a file in 'write binary' mode.

for chunk in res.iter_content(100000):      #this loop is for save downloaded information in hard drive.
    playFile.write(chunk)
