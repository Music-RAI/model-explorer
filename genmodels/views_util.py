from django.core.mail import send_mail

from modelexplorer.settings import CONTACT_EMAILS, EMAIL_HOST_USER

def email_contacts(title, message, from_email=None, tag=None):
    title = f"[Music RAI] [{tag}] {title}" if tag else f"[Music RAI] {title}"
    from_email = from_email if from_email is not None else EMAIL_HOST_USER

    send_mail(title, message, from_email, CONTACT_EMAILS)
