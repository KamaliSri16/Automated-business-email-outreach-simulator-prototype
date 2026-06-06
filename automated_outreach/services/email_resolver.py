class EmailResolver:
    def generate_emails(self, contacts):
        for contact in contacts:
            full_name = contact["person_name"].lower().split()

            first_name = full_name[0]
            last_name = full_name[1]

            domain = contact["company_domain"]

            contact["email"] = (
                f"{first_name}.{last_name}@{domain}"
            )

        return contacts