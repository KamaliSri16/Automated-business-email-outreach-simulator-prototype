from dataclasses import dataclass


@dataclass
class Contact:
    company_domain: str
    company_name: str
    person_name: str
    job_title: str
    linkedin_url: str
    email: str

    def to_dict(self) -> dict:
        return {
            "company_domain": self.company_domain,
            "company_name": self.company_name,
            "person_name": self.person_name,
            "job_title": self.job_title,
            "linkedin_url": self.linkedin_url,
            "email": self.email
        }

    def __str__(self) -> str:
        return (
            f"Company: {self.company_name} ({self.company_domain})\n"
            f"Name: {self.person_name}\n"
            f"Title: {self.job_title}\n"
            f"LinkedIn: {self.linkedin_url}\n"
            f"Email: {self.email}"
        )