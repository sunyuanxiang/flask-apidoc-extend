import unittest
import platform
from flask_apidoc_extend.utils import apidoc_cmd


class TestUtil(unittest.TestCase):
    def test_apidoc_cmd(self):
        if platform.system() == "Windows":
            self.assertNotEqual(apidoc_cmd(),"apidoc")
        else:
            self.assertEqual(apidoc_cmd(),"apidoc")
