from itertools import filterfalse
pegt_board: dict[int, tuple[int, int, int, bool]] = {1:(1,1,1,True),
                                                     2:(2,2,1,True),3:(3,2,2,True),
                                                     4:(1,3,1,True),5:(4,3,2,True),6:(1,3,3,True),
                                                     7:(2,4,1,True), 8:(3,4,2,True),9:(2,4,3,True),10:(3,4,4,True),
                                                     11:(1,5,1,True),12:(4,5,2,True),13:(1,5,3,True),14:(4,5,4,True),15:(1,5,5,True)}
                                           #[jumpValididty, Row, Position, hasPin]
def print_Board(board: dict[int, tuple[int, int, int, bool]]) -> None:
    i = 0
    for i in board:
        if board[i][0] + board[i][2] == 2 and board[i][1]%2 == 0:
            print("\n")
        elif board[i][0] + board[i][2] == 3 and board[i][1]%2 == 1:
            print("\n")
        if board[i][3] == False:
            print(f" {i} ")
        else:
            print(f" |{i}| ")


print_Board(pegt_board)









