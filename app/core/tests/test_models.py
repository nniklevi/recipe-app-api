from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models of  core app

    Args:
        TestCase ([TestCase]): parent class for Django test classes
    """

    def test_create_user_with_email_successful(self):
        """test creation of Django user with email address"""
        email = "nnenad@x.com"
        password = "testPass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if new user nas lowercase domain name in email"""
        email = "nenad@DOMAIN.com"
        user = get_user_model().objects.create_user(
            email=email,
            password="test123",
        )
        self.assertEqual(user.email, email.lower())

    def test_user_invalid_email(self):
        """tests that we raise ValueError exception when blank email is sent as a parameter"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_superuser(self):
        """Test that superuser is properly created"""
        user = get_user_model().objects.create_superuser(
            email="nenad@x.com", password="test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
