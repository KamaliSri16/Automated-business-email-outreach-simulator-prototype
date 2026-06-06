from services.company_discovery import CompanyDiscovery
from services.contact_discovery import ContactDiscovery
from services.email_resolver import EmailResolver
from services.email_generator import EmailGenerator
from services.outreach_sender import OutreachSender


def main():
    print("=" * 60)
    print("AUTOMATED OUTREACH PIPELINE SIMULATION")
    print("=" * 60)

    domain = input("\nEnter company domain: ").strip()

    print("\n[1/5] Discovering similar companies...")
    company_service = CompanyDiscovery()
    companies = company_service.find_similar_companies(domain)

    if not companies:
        print("No companies found.")
        return

    print(f"Found {len(companies)} similar companies.")

    print("\n[2/5] Discovering decision makers...")
    contact_service = ContactDiscovery()
    contacts = contact_service.generate_contacts(companies)

    print(f"Generated {len(contacts)} contacts.")

    print("\n[3/5] Resolving email addresses...")
    email_resolver = EmailResolver()
    contacts = email_resolver.generate_emails(contacts)

    print("Email resolution completed.")

    print("\n[4/5] Campaign Preview")
    print("-" * 60)

    for contact in contacts[:5]:
        print(
            f"{contact['person_name']} | "
            f"{contact['job_title']} | "
            f"{contact['email']}"
        )

    print("-" * 60)
    print(f"Total Contacts: {len(contacts)}")

    confirm = input("\nSend campaign? (y/n): ").lower()

    if confirm != "y":
        print("Campaign cancelled.")
        return

    print("\n[5/5] Sending outreach campaign...")

    email_generator = EmailGenerator()
    sender = OutreachSender()

    sender.send_emails(
        contacts,
        email_generator
    )

    print("\nPipeline execution completed successfully.")


if __name__ == "__main__":
    main()