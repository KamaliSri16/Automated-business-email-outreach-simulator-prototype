import json
import random
from pathlib import Path


class CompanyDiscovery:
    def __init__(self):
        self.data_file = Path("data/companies.json")

    def load_companies(self):
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Company database not found.")
            return []

    def find_similar_companies(self, domain):
        companies = self.load_companies()

        if not companies:
            return []

        # Find the input company
        selected_company = None

        for company in companies:
            if company["domain"].lower() == domain.lower():
                selected_company = company
                break

        # If company not found, choose random companies
        if selected_company is None:
            return random.sample(companies, min(5, len(companies)))

        industry = selected_company["industry"]

        similar_companies = [
            company
            for company in companies
            if company["industry"] == industry
            and company["domain"] != selected_company["domain"]
        ]

        if len(similar_companies) > 5:
            similar_companies = random.sample(similar_companies, 5)

        return similar_companies