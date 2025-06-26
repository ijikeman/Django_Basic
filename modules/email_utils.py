from typing import Optional

class EmailUtils:
    """
    A utility class for email-related operations.
    """

    def extract_domain(self, email: str) -> Optional[str]:
        """
        Extracts the domain from a given email address.

        Args:
            email: The email address string.

        Returns:
            The domain part of the email if valid, otherwise None.
        """
        if not isinstance(email, str):
            return None

        try:
            local_part, domain_part = email.split('@')
            if not local_part or not domain_part or '.' not in domain_part or domain_part.startswith('.'):
                return None
            return domain_part
        except ValueError:
            # .split('@') fails if there is no '@' symbol.
            return None