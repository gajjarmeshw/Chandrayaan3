# For changing the input values change list elements in list named C
class Chandrayaan3:

    # Initializing x, y, z, initial direction and temporary direction using Constructor
    def __init__(self, x, y, z, initial_direction):
        self.x = x
        self.y = y
        self.z = z
        self.initial_direction = initial_direction
        self.temporary_direction = "N"
    # Method for moving forward and backward in various directions

    # Method for moving forward
    def forward_movement(self):
        if self.initial_direction == "N":
            self.y += 1
        elif self.initial_direction == "S":
            self.y -= 1
        elif self.initial_direction == "E":
            self.x += 1
        elif self.initial_direction == "W":
            self.x -= 1    
    
    # Method for moving backward
    def backward_movement(self):
        if self.initial_direction == "N":
            self.y -= 1
        elif self.initial_direction == "S":
            self.y += 1
        elif self.initial_direction == "E":
            self.x -= 1
        elif self.initial_direction == "W":
            self.x += 1
    # Methods for rotationg spacecraft left and right

    # Method for rotating left
    def rotate_left(self):
        if self.initial_direction == "N":
            self.initial_direction = "W"
        elif self.initial_direction == "S":
            self.initial_direction = "E"
        elif self.initial_direction == "E":
            self.initial_direction = "N"
        elif self.initial_direction == "W":
            self.initial_direction = "S"

    # Method for rotating right
    def rotate_right(self):
        if self.initial_direction == "N":
            self.initial_direction = "E"
        elif self.initial_direction == "S":
            self.initial_direction = "W"
        elif self.initial_direction == "E":
            self.initial_direction = "S"
        elif self.initial_direction == "W":
            self.initial_direction = "N"
    
    # Method for moving upward and downward

    # Method for changing direction to up
    def upward_movement(self):
        if self.initial_direction != "U":
            self.temporary_direction = self.initial_direction
            self.initial_direction = "U"
       
    # Method for changing direction to down
    def downward_movement(self):
        if self.initial_direction != "D":
            self.temporary_direction = self.initial_direction
            self.initial_direction = "D"  

# Function for passing commands to operate spacecraft
def movements(chandrayaan3_obj, commands):
    for i in commands:
        if i == "f":
            chandrayaan3_obj.forward_movement()
        elif i == "b":
            chandrayaan3_obj.backward_movement()
        elif i == "l":
            chandrayaan3_obj.rotate_left()
        elif i == "r":
            chandrayaan3_obj.rotate_right()
        elif i == "u":
            chandrayaan3_obj.upward_movement()
        elif i == "d":
            chandrayaan3_obj.downward_movement()
     

# Passing commands through list C
C = ["f","l","b"]
initial_position = (0, 0, 0)
initial_direction = "N"
chandrayaan3_obj = Chandrayaan3(initial_position[0],initial_position[1],initial_position[2], initial_direction)
 
movements(chandrayaan3_obj, C)
print("Final Position -", (chandrayaan3_obj.x, chandrayaan3_obj.y, chandrayaan3_obj.z))
print("Final Direction -", chandrayaan3_obj.initial_direction)
