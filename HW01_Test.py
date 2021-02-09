from HW01 import classify_triangle
import unittest
from math import sqrt


class TestTriangles(unittest.TestCase):

    def test_zne(self):
        # Test zero or negative length of edge (Not even a triangle)
        self.assertEqual(classify_triangle(0, 0, 0), None)
        self.assertEqual(classify_triangle(0, 1, 1), None)
        self.assertEqual(classify_triangle(-2, -2, -3), None)

    def test_equ(self):
        # Test equilateral triangles
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral Triangle")
        self.assertEqual(classify_triangle(3.1, 3.1, 3.1), "Equilateral Triangle")
        self.assertNotEqual(classify_triangle(4, 4, 2), "Equilateral Triangle")

    def test_iso(self):
        # Test isosceles triangles
        self.assertEqual(classify_triangle(5.1, 5.1, 3), "Isosceles Triangle")
        self.assertEqual(classify_triangle(1, 1, sqrt(2)), "Right Isosceles Triangle")
        self.assertNotEqual(classify_triangle(5.1, 5.1, 12), "Isosceles Triangle")   # Not even a triangle
        self.assertNotEqual(classify_triangle(5.1, 5.1, 5.1), "Isosceles Triangle")

    def test_rig(self):
        # Test right triangles
        self.assertEqual(classify_triangle(3, 4, 5), "Right Scalene Triangle")
        self.assertEqual(classify_triangle(12, 5, 13), "Right Scalene Triangle")
        self.assertEqual(classify_triangle(0.3, 0.5, 0.4), "Right Scalene Triangle")
        self.assertEqual(classify_triangle(0.12, 0.05, 0.13), "Right Scalene Triangle")
        self.assertNotEqual(classify_triangle(7, 8, 9), "Right Scalene Triangle")
        self.assertEqual(classify_triangle(1, 1, sqrt(2)), "Right Isosceles Triangle")

    def test_sca(self):
        # Test scalene triangles
        self.assertEqual(classify_triangle(7, 8, 9), "Scalene Triangle")
        self.assertEqual(classify_triangle(3, 4, 5), "Right Scalene Triangle")
        self.assertEqual(classify_triangle(3.10101, 3.10102, 3.10103), "Scalene Triangle")
        self.assertNotEqual(classify_triangle(3.10101, 3.10101, 3.10102), "Scalene Triangle")


if __name__ == '__main__':
    unittest.main()
