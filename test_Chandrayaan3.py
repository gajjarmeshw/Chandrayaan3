import unittest

from Chandrayaan3 import Chandrayaan3, movements

class TestChandrayaan3(unittest.TestCase):
    
    def setUp(self):
        # Initialize a new Chandrayaan3 object before each test
        self.c = Chandrayaan3(0, 0, 0, "N")
        
    # Test forward movement
    def test_forward_movement(self):
        self.c.forward_movement()
        
        # Check if the object's attributes are as expected after forward movement
        self.assertEqual(self.c.x, 0)
        self.assertEqual(self.c.y, 1)
        self.assertEqual(self.c.z, 0)
        self.assertEqual(self.c.initial_direction, "N")
    
    # Test backward movement
    def test_backward_movement(self):
        self.c.backward_movement()
        
        # Check if the object's attributes are as expected after backward movement
        self.assertEqual(self.c.x, 0)
        self.assertEqual(self.c.y, -1)
        self.assertEqual(self.c.z, 0)
        self.assertEqual(self.c.initial_direction, "N")
    
    # Test rotate left
    def test_rotate_left(self):
        self.c.rotate_left()
        
        # Check if the object's attributes are as expected after rotating left
        self.assertEqual(self.c.x, 0)
        self.assertEqual(self.c.y, 0)
        self.assertEqual(self.c.z, 0)
        self.assertEqual(self.c.initial_direction, "W")
    
    # Test rotate right
    def test_rotate_right(self):
        self.c.rotate_right()

        # Check if the object's attributes are as expected after rotating right
        self.assertEqual(self.c.x, 0)
        self.assertEqual(self.c.y, 0)
        self.assertEqual(self.c.z, 0)
        self.assertEqual(self.c.initial_direction, "E")

    # Test upward movement
    def test_upward_movement(self):
        self.c.upward_movement()

        # Check if the object's attributes are as expected after moving upward
        self.assertEqual(self.c.x, 0)
        self.assertEqual(self.c.y, 0)
        self.assertEqual(self.c.z, 0)
        self.assertEqual(self.c.initial_direction, "U")

    # Test downward movement
    def test_downward_movement(self):
        self.c.downward_movement()

        # Check if the object's attributes are as expected after moving downward
        self.assertEqual(self.c.x, 0)
        self.assertEqual(self.c.y, 0)
        self.assertEqual(self.c.z, 0)
        self.assertEqual(self.c.initial_direction, "D")


    # Test movements function
    def test_movements(self):
        # Initialize Chandrayaan3 object
        c = Chandrayaan3(0, 0, 0, "N")

        # Define a sequence of commands
        commands = ["f","r","u","b","r"]

        # Apply the commands
        movements(c, commands)

        # Check the final position and direction
        self.assertEqual((c.x, c.y, c.z), (0, 1, -1)) 
        
        # Expected final position
        self.assertEqual(c.initial_direction, "E") 
        
    def test_movements2(self):
        # Initialize Chandrayaan3 object
        c = Chandrayaan3(4, -2, 0, "W")

        # Define a sequence of commands
        commands = ["l","l","u","r","d","f","j"]

        # Apply the commands
        movements(c, commands)

        # Check the final position and direction
        self.assertEqual((c.x, c.y, c.z), (4, -2, -1)) 
        
        # Expected final positionn
        self.assertEqual(c.initial_direction, "D") 
            
    
if __name__ == "__main__":
    unittest.main()




