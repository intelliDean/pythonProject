import unittest
from Dean.video.functions.bigger import bigger


class AllTest(unittest.TestCase):
    def test_bigger(self):
        assert bigger(3, 5) == 5
        assert bigger(789, 674) == 789
        assert bigger(-1, -5) == -1 
        assert bigger(0, -342) == 0


if __name__ == '__main__':
    unittest.main()
