import unittest
from main import Sphere, Cylinder, Rectangle, Cube


class TestShapes(unittest.TestCase):

    def setUp(self):
        self.sphere = Sphere(5)
        self.cylinder = Cylinder(3, 7)
        self.rectangle = Rectangle(4, 8)
        self.cube = Cube(4)

    # Sphere
    def test_sphere_calculate_area(self):
        self.assertAlmostEqual(self.sphere.calculate_area(), 314.159, places=3)

    def test_sphere_calculate_volume(self):
        self.assertAlmostEqual(self.sphere.calculate_volume(), 523.599, places=3)


    # Cylinder
    def test_cylinder_calculate_area(self):
        self.assertAlmostEqual(self.cylinder.calculate_area(), 188.496, places=3)

    def test_cylinder_calculate_volume(self):
        self.assertAlmostEqual(self.cylinder.calculate_volume(), 197.920, places=3)

    #Rectangle
    def test_rectangle_calculate_area(self):
        self.assertAlmostEqual(self.rectangle.calculate_area(), 32, places=3)

    def test_rectangle_calculate_volume(self):
        self.assertEqual(self.rectangle.calculate_volume(), 0)

    #Cube
    def test_cube_calculate_area(self):
        self.assertAlmostEqual(self.cube.calculate_area(), 96)

    def test_cube_calculate_volume(self):
        self.assertAlmostEqual(self.cube.calculate_volume(), 64)

    #Special
    def test_sphere_zero_radius(self):
        sphere = Sphere(0)
        self.assertEqual(sphere.calculate_area(), 0)
        self.assertEqual(sphere.calculate_volume(), 0)

    def test_cube_unit_size(self):
        cube = Cube(1)
        self.assertEqual(cube.calculate_area(), 6)
        self.assertEqual(cube.calculate_volume(), 1)

    def test_cylinder_zero_height(self):
        cylinder = Cylinder(5, 0)
        self.assertAlmostEqual(cylinder.calculate_area(), 157.080, places=3)
        self.assertEqual(cylinder.calculate_volume(), 0)

    def test_rectangle_square(self):
        square = Rectangle(5, 5)
        self.assertEqual(square.calculate_area(), 25)


if __name__ == '__main__':
    unittest.main()