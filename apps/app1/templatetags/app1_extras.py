from django import template
from modules.email_utils import EmailUtils

register = template.Library()
email_utils = EmailUtils()

@register.filter
def extract_domain(email):
    """
    Extracts the domain from an email address.
    Returns an empty string if the email is invalid, None, or empty.
    """
    if not email:
        return ""
    domain = email_utils.extract_domain(email)
    return domain if domain is not None else ""
