import random

FIRST_NAMES = [
    "John", "Sarah", "Michael", "Emma", "David",
    "Sophia", "James", "Olivia", "Daniel", "Ava"
]

LAST_NAMES = [
    "Smith", "Johnson", "Brown", "Williams", "Jones",
    "Miller", "Davis", "Wilson", "Moore", "Taylor"
]

JOB_TITLES = [
    "CEO",
    "CTO",
    "VP Engineering",
    "VP Product"
]


class ContactDiscovery:
    def generate_contacts(self, companies):
        contacts = []

        for company in companies:
            for title in JOB_TITLES:
                first_name = random.choice(FIRST_NAMES)
                last_name = random.choice(LAST_NAMES)

                contact = {
                    "company_domain": company["domain"],
                    "company_name": company["company"],
                    "person_name": f"{first_name} {last_name}",
                    "job_title": title,
                    "linkedin_url": (
                        f"https://linkedin.com/in/"
                        f"{first_name.lower()}-{last_name.lower()}"
                    ),
                    "email": ""
                }

                contacts.append(contact)

        return contacts