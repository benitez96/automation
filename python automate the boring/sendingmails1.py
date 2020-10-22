import smtplib

conn = smtplib.SMTP('smpt.gmail.com', 587)  #server, port

conn.starttls()         #This encrypts connection.

conn.login('username', 'password')

# sending email     -> return a blank dictionary if everything went ok
conn.sendmail('from', 'to', 'Subject: So long...\n\nDear Dan,\nSo long, and thanks for all the fish.\n\nDan.')

conn.quit()