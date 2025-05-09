from table import Table

if __name__ == '__main__':

    table = Table()
    result = True
    x_axis = None
    y_axis = None
    face = None

    while result == True:
        cmd = input("Enter Command: ")
        if str(cmd).upper() == 'PLACE':
            x_axis = input("Enter x-axis: ")
            y_axis = input("Enter y-axis: ")
            face = input("Input where you want the robot to face initially(NORTH, EAST, SOUTH, WEST): ")

        result, msg = table.execute_cmd(
            cmd=cmd,
            x_axis=x_axis,
            y_axis=y_axis,
            face=face,
        )
        if result:
            table.create_table()
            print(msg)
        else:
            print(msg)
