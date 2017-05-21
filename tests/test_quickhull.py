import unittest
import QuickHull


class TestCase(unittest.TestCase):
    def test_quickhull_box(self):
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

    def test_quickhull_tetrahedron(self):
        points = [
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 0),
            (1, 0, 0),
        ]

        points_inside = [
            (0.1, 0.1, 0.1),
            (0.2, 0.1, 0.4),
            (0.1, 0.4, 0.2),
            (0.3, 0.1, 0.2),
        ]

        test_points = points[0::2] + points_inside + points[1::2]
        vertices, triangles = QuickHull.quick_hull(test_points)

        self.assertEqual(set(vertices), set(points))
        self.assertEqual(len(triangles), 4)

    def test_quickhull_duplicates(self):
        points = [
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 0),
            (1, 0, 0),
        ]

        test_points = points * 10
        vertices, triangles = QuickHull.quick_hull(test_points)

        self.assertEqual(set(vertices), set(points))
        self.assertEqual(len(triangles), 4)

    def test_quickhull_errors_1(self):
        points = [
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 0),
            (1, 0, 0),
            'something else',
        ]

        with self.assertRaises(Exception):
            vertices, triangles = QuickHull.quick_hull(points)

    def test_quickhull_errors_2(self):
        points = [
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 0),
            (1, 0, 0),
            ('a', 'b', 'c'),
        ]

        with self.assertRaises(Exception):
            vertices, triangles = QuickHull.quick_hull(points)


if __name__ == '__main__':
    unittest.main()
