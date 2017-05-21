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

        vertices, triangles = QuickHull.quick_hull(points)
        
        self.assertEqual(set(vertices), set(points))
        self.assertEqual(len(triangles), 12)


if __name__ == '__main__':
    unittest.main()
