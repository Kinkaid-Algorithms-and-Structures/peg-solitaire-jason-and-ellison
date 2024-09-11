from operator import truediv
from xmlrpc.client import boolean

from jupyterlab.semver import valid

from peg_controller import peg_controller
import peg_viewer
from peg_viewer import pegt_board


class peg_referee:
#peg:(value, row, position in row, pegBool)

    pegt_board: dict[int, list[int, int, int, bool]] = {1: (1, 1, 1, True),
                                                        2: (2, 2, 1, True), 3: (3, 2, 2, True),
                                                        4: (1, 3, 1, True), 5: (4, 3, 2, True), 6: (1, 3, 3, True),
                                                        7: (2, 4, 1, True), 8: (3, 4, 2, True), 9: (2, 4, 3, True),10: (3, 4, 4, True),
                                                        11: (1, 5, 1, True), 12: (4, 5, 2, True),13: (1, 5, 3, True), 14: (4, 5, 4, True),15: (1, 5, 5, True)}
    keepgoing = True



    def __init__ (self):
        pass


    def startgame(self):
        a=peg_controller()
        onetoremove = a.remove_first_peg()
        print(onetoremove)
        peg_referee.pegt_board[onetoremove][3] = False

        while peg_referee.keepgoing:
            peg_viewer.print_Board(pegt_board)
            peg_controller.retrieve_value()
            if peg_referee.validity_jump(self, peg_controller.peg_move_to, peg_controller.peg_move_from) and peg_referee.validity_jump_over(self, peg_controller.peg_move_to, peg_controller.peg_move_from):
                peg_referee.peg_mover(self, peg_controller.peg_move_to, peg_controller.peg_move_from,peg_referee.return_jump_over(self, peg_controller.peg_move_to,peg_controller.peg_move_from))
            else:
                print ("This is not a valid move!")
            peg_referee.check_keep_going(self)




    def validity_jump(self, peg_move_to: int, peg_move_from: int) -> bool:
        if  (peg_referee.pegt_board[peg_move_from][0] == peg_referee.pegt_board[peg_move_to][1] and
            abs(peg_referee.pegt_board[peg_move_from][1]- peg_referee.pegt_board[peg_move_to][2])==2 and
            abs(peg_referee.pegt_board[peg_move_from][2]-peg_referee.pegt_board[peg_move_to][3])<=2 and
            peg_referee.pegt_board[peg_move_from][3]==True and peg_referee.pegt_board[peg_move_to][3]==False):
            return True
        else:
            return False

    def validity_jump_over(self, peg_jump_over)->bool:
        if peg_referee.pegt_board[peg_jump_over][3]:
            return True
        else:
            return False


    def return_jump_over(self, peg_move_to:int, peg_move_from:int)->int:

        if peg_referee.pegt_board[peg_move_from][1]>peg_referee.pegt_board[peg_move_to][1]:
            if peg_referee.pegt_board[peg_move_from][2]==peg_referee.pegt_board[peg_move_to][2]:
                for key, value_tuple in peg_referee.pegt_board.items():
                    if value_tuple[1]==peg_referee.pegt_board[peg_move_from][1]+1 and value_tuple[2]==peg_referee.pegt_board[peg_move_from][2]:
                        for key, value_tuple, in peg_referee.pegt_board.items():
                            return key

            elif abs(peg_referee.pegt_board[peg_move_from][2] - peg_referee.pegt_board[peg_move_to][2])==2:
                for key, value_tuple in peg_referee.pegt_board.items():
                    if value_tuple[1]==peg_referee.pegt_board[peg_move_from][1]+1 and value_tuple[2]==peg_referee.pegt_board[peg_move_from][2]+1:
                        for key, value_tuple, in peg_referee.pegt_board.items():
                            return key

        else:
            if peg_referee.pegt_board[peg_move_from][2]==peg_referee.pegt_board[peg_move_to][2]:
                for key, value_tuple in peg_referee.pegt_board.items():
                    if value_tuple[1] == peg_referee.pegt_board[peg_move_from][1] -1 and value_tuple[2] == peg_referee.pegt_board[peg_move_from][2]:
                        for key, value_tuple, in peg_referee.pegt_board.items():
                            return key
            elif abs(peg_referee.pegt_board[peg_move_from][2] - peg_referee.pegt_boardd[peg_move_to][2])==2:
                for key, value_tuple in peg_referee.pegt_board.items():
                    if value_tuple[1] == peg_referee.pegt_board[peg_move_from][1] -1 and value_tuple[2] == peg_referee.pegt_board[peg_move_from][2]-1:
                        for key, value_tuple, in peg_referee.pegt_board.items():
                            return key



    def check_keep_going(self):
        peg_counter = 0;
        for key in peg_referee.pegt_board:
            if (key[3]==True):
                peg_counter+=1

        if peg_counter <=1:
            peg_referee.keepgoing = False
        else:
            peg_counter = 0
            peg_referee.keepgoing = True



    def peg_mover(self,  peg_move_to: int, peg_move_from: int, peg_jump_over:int) -> None:

            peg_referee.pegt_board[peg_move_from][3] = False
            peg_referee.pegt_board[peg_move_to][3] = True
            peg_referee.pegt_board[peg_jump_over][3]=False



