import unittest
from unittest.mock import patch

from greetlab.cli import main


class TestCLI(unittest.TestCase):
    def test_whitespace_name_exits_with_2(self):
        with patch("sys.argv", ["sdt-greet", "--name", "   "]):
            with self.assertRaises(SystemExit) as cm:
                main()
        self.assertEqual(cm.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
