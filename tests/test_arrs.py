import unittest
from utils import arrs
from utils import dicts


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3]), [1, 2, 3])
        self.assertEqual(arrs.my_slice([], 2), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -3, -1), [2, 3])

    def test_get_val(self):
        self.assertEqual(dicts.get_val({"I": "Anton", "F": "Glazunov", "O": "Anatolevich"}, "F", "test"), "Glazunov")
        self.assertEqual(dicts.get_val({"I": "Anton", "F": "Glazunov", "O": "Anatolevich"}, "a"), "git")
        self.assertEqual(dicts.get_val({}, "a"), "git")
        self.assertEqual(dicts.get_val({}), "git")
