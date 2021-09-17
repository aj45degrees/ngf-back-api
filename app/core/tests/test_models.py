from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """Database related tests

    Args:
        TestCase (object): django default to run tests
    """

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email works
        """
        email = 'test@45degrees.dev'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normailized(self):
        """Test the email for a new user is normalized
        """
        email = 'test@45DEGREES.DEV'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test that no email raises an error
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test create a new superuser
        """
        user = get_user_model().objects.create_superuser(
            'test@45degrees.dev',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
