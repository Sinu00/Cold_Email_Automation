# **Telegram Email Scraper and Bulk Job Email Sender**

This repository contains a Python script to help you extract email addresses from a Telegram group and send bulk emails for job applications. The script first extracts the emails from the group's chat messages and then uses SMTP to send job application emails with an attached resume to all the email addresses.

## **Features**
- Extracts email addresses from Telegram group messages.
- Sends personalized job application emails to a list of recipients.
- Attaches a resume to each email.
- Sends emails using **Gmail SMTP** (can be customized for other services).
- Uses **BCC** to prevent revealing email addresses to recipients (important for privacy and preventing spam flags).

## **Requirements**

Before you start, make sure you have the following installed:

- Python 3.x
- Python packages: `smtplib`, `ssl`, `email`, `telethon`, and `re`

### **Install dependencies**
You can install the required Python packages by running the following:

```bash
pip install telethon smtplib pandas
```

## **Setup Instructions**

### 1. **Extract Emails from Telegram Group**
First, you need to extract email addresses from a Telegram group.

1. **Create a Telegram Developer Account**:
   - Go to [my.telegram.org](https://my.telegram.org/) and create an account.
   - Obtain your **API ID** and **API Hash**.

2. **Set up Telegram Client**:
   - Replace the `api_id` and `api_hash` in the script with your credentials.
   - Replace `group_username` with the username or group ID of the Telegram group you want to scrape emails from (e.g., `t.me/itjobs`).

3. **Run the Script** to extract email addresses:
   - Run the script to scrape emails from the specified Telegram group.
   - The emails will be saved in a file called `emails.txt`.

```bash
python telegram_email_scrapper.py
```

This will extract up to **500 messages** and store all the email addresses found in the group in `emails.txt`.

### 2. **Send Bulk Job Application Emails**

1. **Set Up Email Sending**:
   - Open the **Bulk Email Sender** script.
   - Enter your **Gmail** account email in the `EMAIL_SENDER` variable.
   - Use an **App Password** (NOT your regular Gmail password) to avoid security issues. You can generate an App Password [here](https://myaccount.google.com/apppasswords).
   - The script will send emails using **Gmail SMTP server**. If you prefer to use a different SMTP provider, change the `SMTP_SERVER` and `SMTP_PORT` variables.

2. **Configure Email Content**:
   - In the email body, change placeholders like `YourName`, `YourCountry`, `YourSkills`, `YourProject`, etc., with your actual details.
   - Ensure your resume is in the same folder as the script, and update the file name in `resume_path` if needed.

3. **Test the Email First**:
   - Before sending emails to all 300+ contacts, set up a test mode and send an email to yourself first to ensure everything works.
   - Uncomment the test email section (`message["To"] = test_email`) and replace `test_email` with your own email address.

4. **Run the Email Sender Script**:
   - Once you're ready, run the script to send emails to all the extracted email addresses.
   - The emails will be sent using **BCC** to avoid sharing recipients' addresses and preventing spam flags.

```bash
python send_bulk_email.py
```

## **Important Notes**

- **App Password**: If you're using Gmail, make sure to use an **App Password** instead of your regular Gmail password. You can generate it in your Google Account settings.
- **Spam Filters**: Sending bulk emails may trigger spam filters. To avoid this:
  - Use **BCC** to keep recipient email addresses private.
  - Avoid using the same email subject line and body in large quantities.
  - Try sending emails in small batches, rather than all at once.

## **Customization**

You can easily customize the following in the scripts:

- **Email Content**: Personalize the subject and body of the email to better reflect your message.
- **SMTP Settings**: If you're using an email provider other than Gmail, you can update the `SMTP_SERVER` and `SMTP_PORT` settings.
- **Group Username**: Change the `group_username` variable to scrape a different Telegram group.

## **Contributing**

Feel free to fork this repository and make improvements or suggestions. If you encounter any issues, open an issue or submit a pull request.

---
