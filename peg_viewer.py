from itertools import filterfalse

                                           #[jumpValididty, Row, Position, hasPin]
def print_Board(self, board: dict[int, tuple[int, int, int, bool]]) -> None:
    i = 0
    while i < len(board):
        x = board[i]
        if x[i][0] + x[i][2] == 2 and x[i][1]%2 == 0:
            print("\n")
        elif x[i][0] + x[i][2] == 3 and x[i][1]%2 == 1:
            print("\n")
        if x[i][3] == False:
            print(" "+ x + " ")
        else:
            print(" |" + x + "| ")








