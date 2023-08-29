class Chandrayaan3:

    def __init__(self, x, y, z, initial_direction):
        self.x = x
        self.y = y
        self.z = z
        self.initial_direction = initial_direction


    def forward_movement(self):
        if self.initial_direction == "N":
            self.y += 1
        elif self.initial_direction == "S":
            self.y -= 1
        elif self.initial_direction == "E":
            self.x += 1
        elif self.initial_direction == "W":
            self.x -= 1    

    def backward_movement(self):
            if self.initial_direction == "N":
                self.y -= 1
            elif self.initial_direction == "S":
                self.y += 1
            elif self.initial_direction == "E":
                self.x -= 1
            elif self.initial_direction == "W":
                self.x += 1


initial_position = (0, 0, 0)
initial_direction = "N"
chandrayaan3_obj = Chandrayaan3(initial_position[0],initial_position[1],initial_position[2], initial_direction)
 
