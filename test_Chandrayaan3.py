import unittest
from Chandrayaan3 import Chandrayaan3
class TestChandrayaan3(unittest.TestCase):
    def setUp(self):
        # Initialize a new Chandrayaan3 object before each test
        self.chandrayaan3_obj = Chandrayaan3(0, 0, 0, "N")

    def test_forward_movement(self):
        self.chandrayaan3_obj.forward_movement()
        self.assertEqual(self.chandrayaan3_obj.x, 0)
        self.assertEqual(self.chandrayaan3_obj.y, 1)
        self.assertEqual(self.chandrayaan3_obj.z, 0)
        self.assertEqual(self.chandrayaan3_obj.initial_direction, "N")


    def test_backward_movement(self):
        self.chandrayaan3_obj.backward_movement()
        self.assertEqual(self.chandrayaan3_obj.x, 0)
        self.assertEqual(self.chandrayaan3_obj.y, -1)
        self.assertEqual(self.chandrayaan3_obj.z, 0)
        self.assertEqual(self.chandrayaan3_obj.initial_direction, "N")

    def test_rotate_left(self):
        self.chandrayaan3_obj.rotate_left()
        self.assertEqual(self.chandrayaan3_obj.x, 0)
        self.assertEqual(self.chandrayaan3_obj.y, 0)
        self.assertEqual(self.chandrayaan3_obj.z, 0)
        self.assertEqual(self.chandrayaan3_obj.initial_direction, "W")

    def test_rotate_right(self):
        self.chandrayaan3_obj.rotate_right()
        self.assertEqual(self.chandrayaan3_obj.x, 0)
        self.assertEqual(self.chandrayaan3_obj.y, 0)
        self.assertEqual(self.chandrayaan3_obj.z, 0)
        self.assertEqual(self.chandrayaan3_obj.initial_direction, "E")

    def test_upward_movement(self):
        self.chandrayaan3_obj.upward_movement()
        self.assertEqual(self.chandrayaan3_obj.x, 0)
        self.assertEqual(self.chandrayaan3_obj.y, 0)
        self.assertEqual(self.chandrayaan3_obj.z, 0)
        self.assertEqual(self.chandrayaan3_obj.initial_direction, "U")

    def test_downward_movement(self):
        self.chandrayaan3_obj.downward_movement()
        self.assertEqual(self.chandrayaan3_obj.x, 0)
        self.assertEqual(self.chandrayaan3_obj.y, 0)
        self.assertEqual(self.chandrayaan3_obj.z, 0)
        self.assertEqual(self.chandrayaan3_obj.initial_direction, "D")
        
if __name__ == "__main__":
    unittest.main()




