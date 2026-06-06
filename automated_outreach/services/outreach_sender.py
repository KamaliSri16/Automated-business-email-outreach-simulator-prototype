from datetime import datetime
from pathlib import Path


class OutreachSender:
    def __init__(self):
        self.log_directory = Path("logs")
        self.log_directory.mkdir(exist_ok=True)

    def send_emails(self, contacts, email_generator):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        log_file = self.log_directory / f"campaign_{timestamp}.txt"

        sent_count = 0

        with open(log_file, "w", encoding="utf-8") as file:

            file.write("=" * 60 + "\n")
            file.write("AUTOMATED OUTREACH CAMPAIGN REPORT\n")
            file.write("=" * 60 + "\n\n")

            for contact in contacts:

                email_content = email_generator.generate_email(contact)

                print(f"Sending email to {contact['email']}...")
                print("✓ Sent\n")

                file.write(f"TO: {contact['email']}\n")
                file.write(f"SUBJECT: {email_content['subject']}\n")
                file.write("-" * 60 + "\n")
                file.write(email_content["body"])
                file.write("\n\n")
                file.write("=" * 60 + "\n\n")

                sent_count += 1

        print(f"\nCampaign completed successfully.")
        print(f"Emails sent: {sent_count}")
        print(f"Log saved to: {log_file}")

        return sent_count