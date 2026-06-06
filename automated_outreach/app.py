import streamlit as st

from services.company_discovery import CompanyDiscovery
from services.contact_discovery import ContactDiscovery
from services.email_resolver import EmailResolver
from services.email_generator import EmailGenerator
from services.outreach_sender import OutreachSender

st.set_page_config(
    page_title="Automated Outreach Pipeline",
    page_icon="📧",
    layout="wide"
)

st.title("📧 Automated Outreach Pipeline Simulator")
st.markdown(
    "Discover companies, generate contacts, create outreach campaigns, and simulate email delivery."
)

domain = st.text_input(
    "Enter Company Domain",
    placeholder="google.com"
)

if st.button("Launch Campaign"):

    if not domain.strip():
        st.warning("Please enter a company domain.")
        st.stop()

    with st.spinner("Discovering similar companies..."):

        company_service = CompanyDiscovery()
        companies = company_service.find_similar_companies(domain)

    if not companies:
        st.error("No companies found.")
        st.stop()

    st.success(f"Found {len(companies)} similar companies.")

    st.subheader("🏢 Similar Companies")
    st.dataframe(companies, use_container_width=True)

    contact_service = ContactDiscovery()
    contacts = contact_service.generate_contacts(companies)

    email_resolver = EmailResolver()
    contacts = email_resolver.generate_emails(contacts)

    st.subheader("👥 Generated Contacts")
    st.dataframe(contacts, use_container_width=True)

    email_generator = EmailGenerator()

    st.subheader("📨 Email Preview")

    sample_email = email_generator.generate_email(contacts[0])

    st.text_input(
        "Subject",
        sample_email["subject"],
        disabled=True
    )

    st.text_area(
        "Email Body",
        sample_email["body"],
        height=250,
        disabled=True
    )

    if st.button("Send Campaign"):

        sender = OutreachSender()

        count = sender.send_emails(
            contacts,
            email_generator
        )

        st.success(
            f"Campaign completed successfully. {count} emails sent."
        )