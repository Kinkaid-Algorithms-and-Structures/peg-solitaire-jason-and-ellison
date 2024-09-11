import logging, datetime
from KinkaidDecorators import log_start_stop_method
from peg_referee import peg_referee

logging.basicConfig(level=logging.INFO)  # simple version to the output console
# logging.basicConfig(level=logging.DEBUG, filename=f"log {datetime.datetime.now():%m-%d@%H:%M:%S}.txt",
#                     format="%(asctime)s %(levelname)s %(message)s",
#                     datefmt="%H:%M:%S %p --- ")  # more robust, sent to a file cNode = Tuple[int, T]

class PegSolitaireRunner:
    def __init__(self):
        pass

    def main(self):
        print("\nStarting game")
        # add any code you ant to set up variables for the game.
        ref = peg_referee()
        peg_referee.startgame(ref)
        print("\nEnding game ")

game = PegSolitaireRunner()
game.main()




