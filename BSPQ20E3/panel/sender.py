import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .logs import get_logger

def send(recipients, body="New Information available on the website!!!"):
	"""
    Description
    -----------
    Simple email smtp sender

    Parameters
    ----------
    recipients: array of Strings
      The recipients of the email
      default value: " "

    body: str
      Body of the email
      default value: "New Information available on the website!!!"
	"""
	######################### Create a normal email ####################################
	subject = "Good News!"
	bodyE = body
	sender_email = "notjustininsider@gmail.com"
	password = "BSPQ20-E3"
	# Create a multipart message and set headers
	message = MIMEMultipart()
	message["From"] = 'Justin Sider'
	message["To"] =  'HiddenGroup' #', '.join(recipients)
	message["Subject"] = subject
	#message["Bcc"] =  ", ".join(recipients)  # Recommended for mass emails

	# Add body to email

	message.attach(MIMEText(bodyE, "plain"))

	######################### Attach an image  ####################################

	filename = "screen.png"  # In same directory as script

	# Open PDF file in binary mode
	with open(filename, "rb") as attachment:
	    # Add file as application/octet-stream
	    # Email client can usually download this automatically as attachment
	    part = MIMEBase("application", "octet-stream")
	    part.set_payload(attachment.read())

	# Encode file in ASCII characters to send by email    
	encoders.encode_base64(part)

	# Add header as key/value pair to attachment part
	part.add_header(
	    "Content-Disposition",
	    f"attachment; filename= {filename}",
	)

	# Add attachment to message and convert message to string
	message.attach(part)

	######################### Send the created email ####################################
	text = message.as_string()

	# Log in to server using secure context and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
	    server.login(sender_email, password)
	    server.sendmail(sender_email, recipients, text)
	get_logger().info(f"Email sent!")