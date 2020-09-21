#! python3
import re, pyperclip
#To do: 1->Create a regex for phone numbers
#       2->Create a regex for email adresses
#       3->Get the text off the clipboard
#       4->Extract the email/phone from this text
#       5->Copy the extracted email/phone to the clipboard

# Step 1:
phoneNumberRegex = re.compile(r'''
#Number type 415-555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
 ((\d\d\d)|(\(\d\d\d\)))?       #area code(optional)
 (\s|-)                         #first separatos
 \d\d\d                         #fist 3 digits
 -                              #separator
 \d\d\d\d                       #last 4 digits
 (((ext(\.)?\s)|x)              #extension word-part (optional)
  (\d{2,5}))?                   #extension number-part(optional) 
)
''', re.VERBOSE)

# Step 2:
emailRegex = re.compile(r'''
#something@somethig.dom

[a-zA-z0-9_.+]+     #name part
@                   #@ symbol
[a-zA-z0-9_.+]+     #domain part
''', re.VERBOSE)

#Step 3:
text = pyperclip.paste()

#Step 4:
extractedPhones = phoneNumberRegex.findall(text)
extractedEmail = emailRegex.findall(text)
allPhoneNumers = []
for phoneNumer in extractedPhones:
    allPhoneNumers.append(phoneNumer[0])

results = '\n'.join(allPhoneNumers) + '\n'.join(extractedEmail)
pyperclip.copy(results)
