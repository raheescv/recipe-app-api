"""
Test Custom Django Management Commands.
"""

from unittest.mock import patch
from mysql.connector.errors import Error as MysqlError

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch("core.management.commands.wait_for_db.Command.check")
class CommandTests(SimpleTestCase):
    """Text Commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test Waiting for the database if database is ready."""
        patched_check.return_value = True
        call_command("wait_for_db")
        patched_check.assert_called_once_with(databases=["default"])

    @patch("time.sleep")
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test Waiting for the database when getting OperationalErrors."""
        patched_check.side_effect = [MysqlError] * 1 + [OperationalError] * 1 + [True]

        call_command("wait_for_db")
        self.assertEqual(patched_check.call_count, 3)
        patched_check.assert_called_with(databases=["default"])
