## Modules --> pip install imapclient, pip install pyzmail

import imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)    #ssl=True -> encrypts
conn.login('username', 'password')
conn.list_folders()
conn.select_folder('INBOX', readonly=True)
#if readonly = False
conn.delete_messages([UIDs[n:m]])   # list with id messages we want to delete

UIDs = conn.search(['SINCE 20-Aug-2015'])    
'''Most common searching keys: 'ALL', 'BEFORE date', 'ON date', 'SUBJECT string',
'BODY string', 'TEXT string'.
'''
rawMessage = conn.fetch([UIDs[n]], ['BODY[]', 'FLAGS[]'])   #n = any index from uids list

import pyzmail

message = pyzmail.PyzMessage.factory(rawMessage[n][b'BODY[]'])

#== some methods ==#

message.get_subject()

message.get_adresses('from')

message.get_adresses('to')

message.get_adresses('bcc')

message.text_part

message.html_part

message.text_part.get_payload().decode('UTF-8')

message.text_part.charset

