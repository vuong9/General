import smtplib
import time
import win32com.client

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_acct = 'username@gmail.com'
smtp_password = 'password'
tgt_accts = ['user@hotmail.com']
tgt_accts2 = ['username@gmail.com']


def plain_email(subject, contents):
    message = f'Subject: {subject}\n From {smtp_acct}\n'
    message += f'To: {tgt_accts}\n\n{contents.decode()}'
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_acct, smtp_password)

    server.set_debuglevel(1)
    server.sendmail(smtp_acct, tgt_accts, message)
    time.sleep(1)
    server.quit()


def outlook(subject, contents):
    outlook = win32com.client.Dispatch('Outlook.Application')
    message = outlook.CreateItem(0)
    message.DeleteAfterSubmit = True
    message.Subject = subject
    message.Body = contents.decode()
    message.To = tgt_accts2[0]
    message.Send()


if __name__ == '__main__':
    plain_email('testpython',b'Hello World')
    #outlook('test', b'Hello World.')
