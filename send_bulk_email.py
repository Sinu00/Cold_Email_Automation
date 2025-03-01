import smtplib
import ssl
from email.message import EmailMessage

# Email settings
SMTP_SERVER = "smtp.gmail.com"  # For Gmail. Use "smtp.office365.com" for Outlook.
SMTP_PORT = 465  # Use 587 if you don't want SSL.
EMAIL_SENDER = ""  # Replace with your email
EMAIL_PASSWORD = ""  # Use App Password, NOT your actual password

# Load email list from file (for bulk sending later)
with open("emails.txt", "r") as file:
    email_list = [line.strip() for line in file.readlines()]

# ✅ Test Mode: Send only to this email first (before bulk sending)
# test_email = "something@something.com"  # Replace with your test email

# Attach your resume (Make sure it's in the same folder as the script)
resume_path = "Resume.pdf"  # Update with the correct file path if needed

# Email content Change all the place holders like YourName,YourCountry
subject = "Inquiry About Tech Job Opportunities – Available for Immediate Joining"
body = """\
Dear Hiring Team,

I hope you're doing well. My name is YourName, and I’m a Software Developer, currently in YourCountry, actively looking for new opportunities. I wanted to reach out to see if there are any open roles that match my skills or where I can contribute and grow.

A little about me:
💻 Backend & Full-Stack Development – Experience with YourSkills
🖥️ Frontend Skills – Worked with YourSkills
📊 Databases – Hands-on experience with YourSkills
📈 Projects – Developed YourProject

One of my biggest strengths is that I’m a quick learner and always ready to adapt to any technology required by the company. I like to solve problems and take on new challenges, so I’m open to working with any tech stack that helps me contribute effectively.

I’ve attached my resume and GitHub portfolio for your reference. I’d love to discuss any open positions where I could be a good fit. Let me know if there’s a chance to connect!

Looking forward to hearing from you.

Best regards,  
YourName
📍 Currently in YourCountry 
📧 YourEmailID  
📞 YourPhoneNO  
🔗 YourLinkeinURL
🔗 YourGithubURL
"""

# Create email message
message = EmailMessage()
message["From"] = EMAIL_SENDER
message["Subject"] = subject
message.set_content(body)

# Attach Resume
try:
    with open(resume_path, "rb") as resume_file:
        message.add_attachment(
            resume_file.read(),
            maintype="application",
            subtype="pdf",
            filename="YourName_Resume.pdf",
        )
except FileNotFoundError:
    print("⚠️ Resume file not found! Make sure 'resume.pdf' is in the same folder.")

# Start SMTP connection
context = ssl.create_default_context()
with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)

    # ✅ Test: Send email only to your test email first
    # message["To"] = test_email  # Use only one "To" for test
    # server.send_message(message)
    # print(f"✅ Test email sent to {test_email}")

    # 🔴 Use BCC for all recipients to avoid spam flags
    message["Bcc"] = ", ".join(email_list)  # Add all emails to BCC
    server.send_message(message)
    print("✅ All emails sent successfully!")

print("✅ Email process completed!")
