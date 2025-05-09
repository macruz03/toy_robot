# Toy Robot

## Introduction

This project is an implementation of a simple `Toy Robot` application in Python. 

The Robot is placed in a 5x5 tabletop grid. It is free to roam around the surface of the table, but must be prevented from falling to it's destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.

The origin (0,0) can be considered to be the SOUTH WEST most corner.

The Robot accepts the following commands:

 - Place -- To place the `Toy Robot` in the specific grid, and which direction it is facing.
 - Move -- To move the `Toy Robot` one grid in it's current direction.
 - Left -- Turning the `Toy Robot` 90 degrees to the left from it's current direction.
 - Right -- Turning the `Toy Robot` 90 degrees to the right from it's current direction.
 - Report -- Reports where the `Toy Robot` is on the grid and what direction it is currently facing.
 - Exit or Quit -- Ends the program.

## Files

Here are the list of files inside this project:

 - robot.py -- Contains the _Robot_ class and it's functionalities.
 - table.py -- Contains the _Table_ class. It also contains the command execution for the `Toy Robot` and creation of the  gridded `table` .
 - toy_robot.py -- Contains the main executable to run our `Toy Robot`.
 - test_robot.py -- Contains unit testing for our `Toy Robot`.

## Requirements

Additionally the project contains a requirement.txt that contains the required additional `Python` libraries that our `Toy Robot` uses.

 - tabulate -- This library is used to create a clean table grid.
 - pytest -- This library is used to run our `Toy Robot's` unit tests.

## How to Run the Program

 1. Ensure that you have `Python` and `pip` installed in your environment.
 2. Clone the repository to get the code.
 3. Once, cloned, install the requirements via `pip install -r requirements.txt` 
 4. Move to the `Robot` directory in the cloned code.
 5. execute: `python toy_robot.py`
 6. **HAVE FUN!!!**

## How to Run Unit Testing

 1. Make sure you've done items 1~4 in the **How to Run the Program** section.
 2. execute: `pytest test_robot.py -vv`

### Sample Unit Testing Result
```bash
$ pytest.exe test_robot.py -vv
============================================================ test session starts ============================================================
platform win32 -- Python 3.10.11, pytest-7.4.4, pluggy-1.5.0 -- C:\codes\iress\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\codes\robot
plugins: anyio-4.3.0
collected 11 items

test_robot.py::TestTableAndRobot::test_place[a-b-south-Can't read that, my coordinates should be a number. a,b.] PASSED                [  9%] 
test_robot.py::TestTableAndRobot::test_place[1-b-south-Can't read that, my coordinates should be a number. 1,b.] PASSED                [ 18%] 
test_robot.py::TestTableAndRobot::test_place[a-2-south-Can't read that, my coordinates should be a number. a,2.] PASSED                [ 27%] 
test_robot.py::TestTableAndRobot::test_place[1-2-Mac-I don't know this direction: Mac, Wait, is this new!?] PASSED                     [ 36%] 
test_robot.py::TestTableAndRobot::test_place[1-5-north-This coordinates 1,5 are way too low or too high for me.] PASSED                [ 45%] 
test_robot.py::TestTableAndRobot::test_place[1-2-west-Hello, I'm at 1,2; facing west.] PASSED                                          [ 54%]
test_robot.py::TestTableAndRobot::test_move PASSED                                                                                     [ 63%] 
test_robot.py::TestTableAndRobot::test_move_edge PASSED                                                                                [ 72%] 
test_robot.py::TestTableAndRobot::test_left PASSED                                                                                     [ 81%] 
test_robot.py::TestTableAndRobot::test_right PASSED                                                                                    [ 90%] 
test_robot.py::TestTableAndRobot::test_report PASSED                                                                                   [100%] 

============================================================ 11 passed in 0.05s =============================================================
```