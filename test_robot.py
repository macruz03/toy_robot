import pytest
from table import Table

class TestTableAndRobot:
    table = Table()

    @pytest.mark.parametrize(
        "x, y, face, expected",
        [
            ("a", "b", "south", "Can't read that, my coordinates should be a number. a,b."),
            ("1", "b", "south", "Can't read that, my coordinates should be a number. 1,b."),
            ("a", "2", "south", "Can't read that, my coordinates should be a number. a,2."),
            ("1", "2", "Mac", "I don't know this direction: Mac, Wait, is this new!?"),
            ("1", "5", "north", "This coordinates 1,5 are way too low or too high for me."),
            ("1", "2", "west", "Hello, I'm at 1,2; facing west."),
        ]
    )
    def test_place(self, x, y, face, expected):
        assert self.table.execute_cmd("PLACE", x_axis=x, y_axis=y, face=face)[1] == expected

    def test_move(self):
        expected = "Okay, I'm now moving to 0,2 facing west."
        assert self.table.execute_cmd("MOVE")[1] == expected

    def test_move_edge(self):
        self.table.execute_cmd("PLACE", x_axis=0, y_axis=4, face="north")
        expected = "I'm not hitting that wall! I'm staying put!"
        assert self.table.execute_cmd("MOVE")[1] == expected
    
    def test_left(self):
        expected = "My current heading is SOUTH."
        assert self.table.execute_cmd("LEFT")[1] == expected

    def test_right(self):
        expected = "My current heading is WEST."
        assert self.table.execute_cmd("RIGHT")[1] == expected

    def test_report(self):
        expected = "I am at: x-axis: 0 y-axis: 2. My current heading is: WEST."
        assert self.table.execute_cmd("REPORT")[1] == expected