
class peg_controller:

    peg_move_from = 0
    peg_move_to = 0
    first_remove = 0


    def __init__(self):
        pass

    def retrieve_value(self):
        peg_controller.peg_move_from = input("What peg would you like to move? Please note that numbers with brackets represent holes that have a peg in it ex. [12].")
        peg_controller.peg_move_to = input("Where would you like to move that peg to. Please note you can only jump a peg over one hole that has a peg in it and you must end in an open hole represented by a number without brackets ex. 12. ")

    def remove_first_peg(self):
        peg_controller.first_remove = input("What number peg would you like to remove to start the game?")
        print(peg_controller.first_remove)