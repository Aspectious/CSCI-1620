import unittest
from area import *

class AreaTestCases(unittest.TestCase):

    def test_strparse(self):
        # Circle
        self.assertRaises(ValueError, circle, "h")
        
        # Square
        self.assertRaises(ValueError, square, "p")
        
        # Rectangle
        self.assertRaises(ValueError, rectangle, "a", "b")
        self.assertRaises(ValueError, rectangle, "k", 7)
        self.assertRaises(ValueError, rectangle, 9.00, "y")

        #Triangle
        self.assertRaises(ValueError, triangle, "a", "b")
        self.assertRaises(ValueError, triangle, 8, "o")
        self.assertRaises(ValueError, triangle, "p", 1.9)


    def test_negative(self):
        #Circle
        self.assertRaises(TypeError, circle, "-1")
        
        # Square
        self.assertRaises(TypeError, square, -49)
        
        # Rect
        self.assertRaises(TypeError, rectangle, "-1", -1)
        self.assertRaises(TypeError, rectangle, -1, "1")
        self.assertRaises(TypeError, rectangle, 1, -1)

        #Triangle
        self.assertRaises(TypeError, triangle, "-1", "-1")
        self.assertRaises(TypeError, triangle, "-1", 1)
        self.assertRaises(TypeError, triangle, 1, "-1")
    

    def test_zero(self):
        #Circle
        self.assertRaises(TypeError, circle, 0)
        
        # Square
        self.assertRaises(TypeError, square, "0")
        
        # Rect
        self.assertRaises(TypeError, rectangle, "0", "0")
        self.assertRaises(TypeError, rectangle, "0", 1)
        self.assertRaises(TypeError, rectangle, "1", "0")

        #Triangle
        self.assertRaises(TypeError, triangle, "0", "0")
        self.assertRaises(TypeError, triangle, 0, "1")
        self.assertRaises(TypeError, triangle, 1, 0)
        

    def test_pos(self):

        # I added delta values of varying amounts to test for rounding and for assertAlmostEqual

        #circle
        self.assertEqual(circle(1), math.pi)
        self.assertAlmostEqual(circle(9.8), 301.72, delta=0.01)
        
        #square
        self.assertEqual(square(1), 1)
        self.assertAlmostEqual(square(491.284), 241359.9, delta=0.1)

        #rectangle
        self.assertEqual(rectangle(8, 8), square(8))
        self.assertEqual(rectangle(4.2, 8), 33.6)
        self.assertAlmostEqual(rectangle(21.4, 16.3), 348, delta=1)
        self.assertAlmostEqual(rectangle(29, 9.8), 284.2, delta=0.1)

        #triangle
        self.assertEqual(triangle(4, 3), 6)
        self.assertEqual(triangle(4.2, 8), 33.6/2)
        self.assertAlmostEqual(triangle(21.4, 16.3), 174, delta=1)
        self.assertAlmostEqual(triangle(29, 9.8), 142.1, delta=0.1)

if __name__ == "__main__":
    unittest.main()
