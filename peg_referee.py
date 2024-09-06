from operator import truediv
from xmlrpc.client import boolean

from jupyterlab.semver import valid

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
    else:
        return False

def validity_jump_over(self, peg_jump_over)->bool:
    if pegt_board.get(self,peg_jump_over)[3] == True:
        return True
    else:
        return False


def return_jump_over(self, peg_move_to:int, peg_move_from:int)->int:

    if pegt_board.get(self, peg_move_from)[1]>pegt_board.get(self, peg_move_to)[1]:
        if pegt_board.get(self, peg_move_from)[2]==pegt_board.get(self, peg_move_to)[2]:
            for key, value_tuple in pegt_board.items():
                if value_tuple[1]==pegt_board.get(self,peg_move_from)[1]+1 and value_tuple[2]==pegt_board.get(self,peg_move_from)[2]:
                    for key, value_tuple, in pegt_board.items():
                        return key

        elif abs(pegt_board.get(self, peg_move_from)[2] - pegt_board.get(self, peg_move_to)[2])==2:
            for key, value_tuple in pegt_board.items():
                if value_tuple[1]==pegt_board.get(self,peg_move_from)[1]+1 and value_tuple[2]==pegt_board.get(self,peg_move_from)[2]+1:
                    for key, value_tuple, in pegt_board.items():
                        return key

    else:
        if pegt_board.get(self, peg_move_from)[2]==pegt_board.get(self, peg_move_to)[2]:
            for key, value_tuple in pegt_board.items():
                if value_tuple[1] == pegt_board.get(self, peg_move_from)[1] -1 and value_tuple[2] == pegt_board.get(self,peg_move_from)[2]:
                    for key, value_tuple, in pegt_board.items():
                        return key
        elif abs(pegt_board.get(self, peg_move_from)[2] - pegt_board.get(self, peg_move_to)[2])==2:
            for key, value_tuple in pegt_board.items():
                if value_tuple[1] == pegt_board.get(self, peg_move_from)[1] -1 and value_tuple[2] == pegt_board.get(self,peg_move_from)[2]-1:
                    for key, value_tuple, in pegt_board.items():
                        return key



def check_keep_going(peg_Board: dict[int, bool]) -> bool:
    peg_counter = 0;
    for key in peg_Board:
        if (key[3]==True):
            peg_counter+=1;

    if peg_counter <=1:
        return False
    else:
        peg_counter = 0
        return True

def final_validity (self, validity_to_move, validity_to_jump):
    if validity_to_move and validity_to_jump:
        return True
    else:
        return False


def peg_mover(self, validity_move: bool, peg_move_to: int, peg_move_from: int, peg_jump_over:int) -> None:
    if validity_move:
        pegt_board[peg_move_from][3] = False
        pegt_board[peg_move_to][3] = True
        pegt_board[peg_jump_over][3]=False
    else:
        print("This is not a valid move!")


