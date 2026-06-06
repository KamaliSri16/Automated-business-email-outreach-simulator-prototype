class EmailGenerator:
    def generate_email(self, contact):
        subject = (
            f"Partnership Opportunity with {contact['company_name']}"
        )

        body = f"""
Hello {contact['person_name']},

I hope you're doing well.

I came across {contact['company_name']} and was impressed by the work your team is doing.

We help organizations improve customer engagement, automate outreach processes, and scale communication efficiently.

I would love to connect and discuss potential opportunities for collaboration.

Looking forward to hearing from you.

Best Regards,
Automated Outreach Team
"""

        return {
            "subject": subject,
            "body": body.strip()
        }