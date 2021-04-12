from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with a email is successfull"""
        email = "test@gmail.com"
        password = "pass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test a email for a new user is normalized """
        email = "test@GMAIL.com"
        user = get_user_model().objects.create_user(email, "myPass123")
        self.assertEqual(user.email, email.lower())
