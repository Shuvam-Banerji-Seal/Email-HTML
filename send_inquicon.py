import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Credentials
sender_email = "sbs22ms076@iiserkol.ac.in"
receiver_email = "purbarunmondal@gmail.com"
password = "waw78tew" # Warning: Highly recommended to use environment variables or App Passwords

# Paths
BASE_DIR = "/home/shuvam/codes/Email-HTML"
html_file_path = os.path.join(BASE_DIR, "inquicon/inquicon_invitation.html")
poster1_path = os.path.join(BASE_DIR, "assets/1.svg")
poster2_path = os.path.join(BASE_DIR, "assets/2.svg")
logo_path = os.path.join(BASE_DIR, "assets/SlashDot Main logo noBG W-01-02.png")

# Read HTML content
with open(html_file_path, "r") as file:
    html_content = file.read()

# Set up the MIME message
msg = MIMEMultipart("related")
msg["Subject"] = "👾 Mission: Anime CAPTCHA - Inquicon 2025 x Slashdot"
msg["From"] = f"Slashdot Programming Club <{sender_email}>"
msg["To"] = receiver_email

# Create the HTML part
msg_html = MIMEText(html_content, "html")
msg.attach(msg_html)

# Add posters as attachments if needed, but for "embedding" usually we use CID
# Note: Gmail support for SVG as CID varies. Using remote URLs (already in HTML) is more reliable.
# If you want to use local paths, you'd replace the URLs with 'cid:poster1' etc.

# Send the email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
