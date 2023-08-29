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


def movements(chandrayaan3_obj, commands):
    for i in commands:
        if i == "f":
            chandrayaan3_obj.forward_movement()
        elif i == "b":
            chandrayaan3_obj.backward_movement()


C = ["f"]
initial_position = (0, 0, 0)
initial_direction = "N"
chandrayaan3_obj = Chandrayaan3(initial_position[0],initial_position[1],initial_position[2], initial_direction)
 
movements(chandrayaan3_obj, C)
print("Final Position -", (chandrayaan3_obj.x, chandrayaan3_obj.y, chandrayaan3_obj.z))
print("Final Direction -", chandrayaan3_obj.initial_direction)
