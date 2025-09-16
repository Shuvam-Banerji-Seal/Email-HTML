import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gmail credentials
sender_email = "sbs22ms076@iiserkol.ac.in"
receiver_email = "purbarunmondal@gmail.com"
password = "waw78tew"

# Read HTML content from a file
with open("/home/shuvam/codes/Email-HTML/Drug_the_Underugged2.html", "r") as file:
    html_content = file.read()

# Set up the MIME message
msg = MIMEMultipart("alternative")
msg["Subject"] = "HTML Email"
msg["From"] = sender_email
msg["To"] = receiver_email

# Attach the HTML content
msg.attach(MIMEText(html_content, "html"))

# Send the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("Email sent successfully!")