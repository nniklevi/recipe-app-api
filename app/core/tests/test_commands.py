from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTest(TestCase):
    """test commands done in command line

    Args:
        TestCase ([type]): [base Django test class]
    """

    def test_wait_for_db_ready(self):
        """Test waiting for DB when DB is available"""
        with patch("django.db.utils.ConnectionHandler.__getitem__") as gi:
            gi.return_value = True
            call_command("wait_for_db")
            self.assertEqual(gi.call_count, 1)

    @patch("time.sleep", return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db. Five failures and sixth time pass"""
        number_of_failures = 5
        with patch("django.db.utils.ConnectionHandler.__getitem__") as gi:
            gi.side_effect = [OperationalError] * number_of_failures + [True]
            call_command("wait_for_db")
            self.assertEqual(gi.call_count, number_of_failures + 1)
