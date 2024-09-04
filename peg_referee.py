from operator import truediv
from xmlrpc.client import boolean

#peg:(value, row, position in row, pegBool)
pegt_board: dict[int, tuple[int, int, int, bool]] = {1:(1,1,1,True),
                                                     2:(2,2,1,True),3:(3,2,2,True),
                                                     4:(1,3,1,True),5:(4,3,2,True),6:(1,3,3,True),
                                                     7:(2,4,1,True), 8:(3,4,2,True),9:(2,4,3,True),10:(3,4,4,True),
                                                     11:(1,5,1,True),12:(4,5,2,True),13:(1,5,3,True),14:(4,5,4,True),15:(1,5,5,True)}



def validity_jump(self, peg_move_to: int, peg_move_from: int) -> bool:
    if (pegt_board.get(self,peg_move_from)[0] == pegt_board.get(self,peg_move_to)[1] and
        abs(pegt_board.get(self,peg_move_from)[1]- pegt_board.get(self,peg_move_to)[2])==2 and
        abs(pegt_board.get(self, peg_move_from[2])-pegt_board.get(self, peg_move_to[3]))<=2 and
        pegt_board.get(self, peg_move_from[3]==True and pegt_board.get(self,peg_move_to[3]==False))):

        return True


def check_Keep_Going(self, peg_Board: dict[int, bool]) -> bool:
    pass

def peg_mover(self, validity_move: bool, peg_move_to: int, peg_move_from: int) -> None:
    pass
