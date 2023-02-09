import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def main():

	link = 'https://www.google.com/'
	email = MIMEText(f'Hi There,<br><br>Please view this link <a href={link}>here</a> to prepare for tomorrow evening<br><br>Thanks,<br>Aaron<br><br>Note: This is an automatic email','html')
	email['Subject'] = 'Hi There'
	email['To'] = me
	email['From'] = me
	
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(me,mypass)
	

	server.sendmail(from_addr = me, to_addrs = me, msg = email.as_string())

	server.quit()
	print('email sent')


def error(error_message):

	print(error_message)

if __name__ == "__main__":
	try:

		server = smtplib.SMTP('smtp.gmail.com', 587)
		me = #YOUR EMAIL ACCOUNT
		you = #RECEIVER'S EMAIL ACCOUNT
		mypass = #YOUR GMAIL PASS
		now = datetime.datetime.now()
		print(f'starting now at {now}')
		main()
		print('all set')
	except BaseException as be:
		print(str(be))
		error(str(be))
