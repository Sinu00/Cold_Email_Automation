from telethon.sync import TelegramClient
import re

# Replace these with your API credentials
api_id = 0  # Your API ID from my.telegram.org
api_hash = ""  # Your API Hash from my.telegram.org
group_username = "itjobs"  # Replace with the group's username or ID like t.me/itjobs then username is itjobs

# Start the Telegram client
client = TelegramClient("session_name", api_id, api_hash)

# Function to extract email IDs using regex
def extract_emails(text):
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

with client:
    messages = client.get_messages(group_username, limit=500)  # Fetch last 500 messages
    emails = []  # List to maintain order

    for msg in messages:
        if msg.text:
            extracted = extract_emails(msg.text)
            if extracted:
                emails.extend(extracted)  # Maintain order (latest first)

    # Remove duplicates while keeping order
    seen = set()
    sorted_emails = [email for email in emails if not (email in seen or seen.add(email))]

    # Save emails to a file
    with open("emails.txt", "w") as file:
        file.write("\n".join(sorted_emails))

    print(f"Extracted {len(sorted_emails)} emails. Check emails.txt")
