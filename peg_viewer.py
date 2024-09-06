from itertools import filterfalse
pegt_board: dict[int, tuple[int, int, int, bool]] = {1:(1,1,1,True),
                                                     2:(2,2,1,False),3:(3,2,2,True),
                                                     4:(1,3,1,True),5:(4,3,2,True),6:(1,3,3,True),
                                                     7:(2,4,1,True), 8:(3,4,2,True),9:(2,4,3,True),10:(3,4,4,True),
                                                     11:(1,5,1,True),12:(4,5,2,True),13:(1,5,3,True),14:(4,5,4,True),15:(1,5,5,True)}
                                           #[jumpValididty, Row, Position, hasPin]
def print_Board(board: dict[int, tuple[int, int, int, bool]]) -> None:
    newLine = (1,2,4,7,11)
    for i in board:
        if i in newLine:
            print("\n", end = "")
            if i == 1:
                print("            ", end = "")
            if i == 2:
                print("         ", end = "")
            if i == 4:
                print("       ", end = "")
            if i == 7:
                print("    ", end = "")
            if i == 11:
                print("", end = "")
        if board[i][3] == False:
            print(f"  {i}  ", end = "")
        else:
            print(f" |{i}| ", end = "")


print_Board(pegt_board)









