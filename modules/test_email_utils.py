import unittest
from modules.email_utils import EmailUtils

class TestEmailUtils(unittest.TestCase):

    def test_extract_domain(self):
        utils = EmailUtils()
        self.assertEqual(utils.extract_domain("test@example.com"), "example.com")
        self.assertEqual(utils.extract_domain("user.name@subdomain.example.co.uk"), "subdomain.example.co.uk")
        self.assertIsNone(utils.extract_domain("invalid-email"))
        self.assertIsNone(utils.extract_domain("@example.com"))
        self.assertIsNone(utils.extract_domain("test@.com"))

if __name__ == '__main__':
    unittest.main()
