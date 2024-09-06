def __init__(self):
    peg_move_from: int = 0
    peg_move_to: int = 0


def retrieve_value():
    peg_move_from = input("What peg would you like to move? Please note that numbers with brackets represent holes that have a peg in it ex. [12].")
    peg_move_to = input("Where would you like to move that peg to. Please note you can only jump a peg over one hole that has a peg in it and you must end in an open hole represented by a number without brackets ex. 12. ")

