# Email Sender

A simple Python script that sends an email containing a link to the recipient using the SMTP library.

## Requirements
import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

import datetime

## Usage
Replace the placeholder values of _'me'_, _'mypass'_, and _'you'_ with your email account and gmail app password, and the recipient's email respectively.

#### GMAIL APP PASSWORD
Instructions on how to obtain your gmail app password can be found [here](https://towardsdatascience.com/automate-sending-emails-with-gmail-in-python-449cc0c3c317)

Run the script using the command python email_sender.py
Check your inbox for the email sent by the script.

## How it works
The script uses the smtplib library to connect to the SMTP server of Gmail. After a successful connection, it logs in to the Gmail account using the credentials provided.

Then, the script creates an email object and populates the necessary fields such as the subject, sender, and recipient. The sample email contains a link to Google.com, and the body of the email is written in HTML format.

Finally, the script sends the email and disconnects from the SMTP server.

## Error Handling
In case of any errors, the error message will be printed, and the error function will be called with the error message as the argument.

## Conclusion
This script demonstrates the basic usage of the smtplib library to send an email and can be modified to fit various use cases.