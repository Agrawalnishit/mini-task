# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Your email credentials
# sender_email = "n9602168@gmail.com"
# sender_password = "nnnlwqgwnljmvenc"
# receiver_email = "agrawalnishit09@gmail.com"

# # Create the message
# message = MIMEMultipart()
# message["From"] = sender_email
# message["To"] = receiver_email
# message["Subject"] = "Test Email from Python"

# # Add email body
# body = "This is a test email sent from Python using SMTP."
# message.attach(MIMEText(body, "plain"))

# # Connect to Gmail SMTP server and send
# try:
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(sender_email, sender_password)
#     server.sendmail(sender_email, receiver_email, message.as_string())
#     server.quit()
#     print("Email sent successfully!")
# except Exception as e:
#     print(f"Error: {e}")




#===================================================================================================
#===================================================================================================
#                             send resume in pdf format 
#===================================================================================================
#===================================================================================================





import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Email credentials
sender_email = "n9602168@gmail.com"
sender_password = "nnnlwqgwnljmvenc"
receiver_email = "agrawalnishit09@gmail.com"

# Create email message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Resume Submission"

# Email body text
body = "Hi,\n\nPlease find my resume attached.\n\nBest regards,\nYour Name"
msg.attach(MIMEText(body, "plain"))

# Attach PDF
filename = "C:/Users/nishi/Downloads/8085 Microprocessor Unit 1 Final.pdf"  # Path to your resume
with open(filename, "rb") as f: # open file in  read format in binary form 
    part = MIMEApplication(f.read(), _subtype="pdf")
    part.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(part)

# Send the email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()
    print("Email with resume sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
