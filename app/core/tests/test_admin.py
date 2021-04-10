from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class TestUserAdmin(TestCase):
    """Test Django Admin interface

    Args:
        TestCase ([type]): [description]
    """

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            "nenad@x.com",
            "test123",
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user1@x.com",
            password="test123",
            name="Test User Full Name",
        )

    def test_users_listed(self):
        """Test that users are listed on admin page"""
        url = reverse("admin:core_user_changelist")  # default Django URL for user list
        user_list = self.client.get(url)

        self.assertContains(user_list, self.user.name)
        self.assertContains(user_list, self.user.email)