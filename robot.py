class Robot:
    FACE = ['NORTH', 'EAST', 'SOUTH', 'WEST']
    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = 'NORTH'
    
    # Place the robot within the specific coordinates and indicate where it is facing.
    def place(self, x_axis, y_axis, facing):
        self.x = x_axis
        self.y = y_axis
        self.facing = facing
            
    # Move the robot one space in the direction it is facing.
    def move(self):
        face = self.facing.upper()
        moved = True
        if face == 'NORTH':
            # Move 1 space up
            if (int(self.y) + 1) > 4:
                moved = False
            else:
                self.y = int(self.y) + 1

        elif face == 'EAST':
            # Move 1 space left
            if (int(self.x) + 1) > 4:
                moved = False
            else:
                self.x = int(self.x) + 1

        elif face == 'SOUTH':
            # Move 1 space down
            if (int(self.y) - 1) < 0:
                moved = False
            else:
                self.y = int(self.y) - 1
        elif face == 'WEST':
            # Move 1 space right
            if (int(self.x) - 1) < 0:
                moved = False
            else:
                self.x = int(self.x) - 1

        return moved
    
    # Rotate the robot facing 90 degrees to the left of it's current face.
    def left(self):
        # We will try to get the index minus one (left) of the current face.
        # By using modulo 4, we can get to circular list.
        # If value of modulo is negative, the result will be the negative value minus the divisor (modulo).
        # E.g. -1 % 4 is -.25, rounded down to floor of -1. 
        self.facing = self.FACE[(self.FACE.index(self.facing.upper()) - 1) % 4]
    
    # Rotate the robot facing 90 degrees to the right of it's current face.
    def right(self):
        # We will try to get the index plus one (right) of the current face.
        # By using modulo 4, we can get to circular list.
        self.facing = self.FACE[(self.FACE.index(self.facing.upper()) + 1) % 4]
    
    # Report the current coordinates and face of the robot.
    def report(self):
        return (
            "I am at: x-axis: " + str(self.x) + 
            " y-axis: " + str(self.y) + 
            ". My current heading is: " + self.facing + 
            "."
        )