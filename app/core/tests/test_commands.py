from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase
from psycopg2 import OperationalError as Psycopg2Error


@patch("core.management.commands.wait_for_db.Command.check")
class CommandsTests(SimpleTestCase):
    def test_wait_for_db_ready(self, check_mock):
        """Test waiting for db when db is available"""
        check_mock.return_value = True
        call_command("wait_for_db")
        check_mock.assert_called_once_with(databases=["default"])

    @patch("time.sleep")
    def test_wait_for_db_not_ready(self, patched_sleep, check_mock):
        """Test waiting for db when db is not available"""
        check_mock.side_effect = [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]
        call_command("wait_for_db")
        self.assertEqual(check_mock.call_count, 6)
        check_mock.assert_called_with(databases=["default"])
