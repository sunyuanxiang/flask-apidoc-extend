import unittest
import platform
from flask_apidoc_extend.utils import apidoc_cmd, sort_app_data


class TestUtil(unittest.TestCase):
    def test_apidoc_cmd(self):
        if platform.system() == "Windows":
            self.assertNotEqual(apidoc_cmd(), "apidoc")
        else:
            self.assertEqual(apidoc_cmd(), "apidoc")

    def test_sort_app_data(self):
        data_obj = [{'name': '2', 'group': "A"},
                    {'name': '3', 'group': 'B'},
                    {'name': '', 'group': 'B'},
                    {'name': '1', 'group': 'A'}]
        order = ['2', 'B']
        target1 = iter([{'name': '3', 'group': 'B'},
                        {'name': '2', 'group': "A"},
                        {'name': '1', 'group': 'A'}])
        target2 = iter([{'name': '2', 'group': "A"},
                        {'name': '1', 'group': 'A'},
                        {'name': '3', 'group': 'B'}])
        for _, data in sort_app_data(data_obj, order):
            for value in data:
                self.assertEqual(value, next(target1))
        for _, data in sort_app_data(data_obj):
            for value in data:
                self.assertEqual(value, next(target2))
