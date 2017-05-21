import unittest
import QuickHull


class TestCase(unittest.TestCase):
    def test_quickhull(self):
        points = [
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 0),
            (0, 1, 1),
            (1, 0, 0),
            (1, 0, 1),
            (1, 1, 0),
            (1, 1, 1),
        ]

        vert, idx = QuickHull.quick_hull(points)


if __name__ == '__main__':
    unittest.main()
