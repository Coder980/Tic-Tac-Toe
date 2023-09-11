import random

class AI:
    def __init__(self):
        self.piece = "O"
        self.pieces = []

    def turn(self, pieces):
        self.pieces = pieces
        if ((self.pieces[0] == "X" and self.pieces[1] == "X") or (self.pieces[0] == "O" and self.pieces[1] == "O")) \
                and self.pieces[2] == " ":
            return 3
        elif ((self.pieces[3] == "X" and self.pieces[4] == "X") or (self.pieces[3] == "O" and self.pieces[4] == "O")) \
                and self.pieces[5] == " ":
            return 6
        elif ((self.pieces[6] == "X" and self.pieces[7] == "X") or (self.pieces[6] == "O" and self.pieces[7] == "O")) \
                and self.pieces[8] == " ":
            return 9
        elif ((self.pieces[1] == "X" and self.pieces[2] == "X") or (self.pieces[1] == "O" and self.pieces[2] == "O")) \
                and self.pieces[0] == " ":
            return 1
        elif ((self.pieces[4] == "X" and self.pieces[5] == "X") or (self.pieces[4] == "O" and self.pieces[5] == "O")) \
                and self.pieces[3] == " ":
            return 4
        elif ((self.pieces[7] == "X" and self.pieces[8] == "X") or (self.pieces[7] == "O" and self.pieces[8] == "O")) \
                and self.pieces[6] == " ":
            return 7
        elif ((self.pieces[0] == "X" and self.pieces[3] == "X") or (self.pieces[0] == "O" and self.pieces[3] == "O")) \
                and self.pieces[6] == " ":
            return 7
        elif ((self.pieces[1] == "X" and self.pieces[4] == "X") or (self.pieces[1] == "O" and self.pieces[4] == "O")) \
                and self.pieces[7] == " ":
            return 8
        elif ((self.pieces[2] == "X" and self.pieces[5] == "X") or (self.pieces[2] == "O" and self.pieces[5] == "O")) \
                and self.pieces[8] == " ":
            return 9
        elif ((self.pieces[3] == "X" and self.pieces[6] == "X") or (self.pieces[3] == "O" and self.pieces[6] == "O")) \
                and self.pieces[0] == " ":
            return 1
        elif ((self.pieces[4] == "X" and self.pieces[7] == "X") or (self.pieces[4] == "O" and self.pieces[7] == "O")) \
                and self.pieces[1] == " ":
            return 2
        elif ((self.pieces[5] == "X" and self.pieces[8] == "X") or (self.pieces[5] == "O" and self.pieces[8] == "O")) \
                and self.pieces[2] == " ":
            return 3
        elif ((self.pieces[0] == "X" and self.pieces[4] == "X") or (self.pieces[0] == "O" and self.pieces[4] == "O")) \
                and self.pieces[8] == " ":
            return 9
        elif ((self.pieces[4] == "X" and self.pieces[8] == "X") or (self.pieces[4] == "O" and self.pieces[8] == "O")) \
                and self.pieces[0] == " ":
            return 1
        elif ((self.pieces[2] == "X" and self.pieces[4] == "X") or (self.pieces[2] == "O" and self.pieces[4] == "O")) \
                and self.pieces[6] == " ":
            return 7
        elif ((self.pieces[4] == "X" and self.pieces[6] == "X") or (self.pieces[4] == "O" and self.pieces[6] == "O")) \
                and self.pieces[2] == " ":
            return 3
        elif ((self.pieces[0] == "X" and self.pieces[6] == "X") or (self.pieces[0] == "O" and self.pieces[6] == "O")) \
                and self.pieces[3] == " ":
            return 4
        elif ((self.pieces[1] == "X" and self.pieces[7] == "X") or (self.pieces[1] == "O" and self.pieces[7] == "O")) \
                and self.pieces[4] == " ":
            return 5
        elif ((self.pieces[2] == "X" and self.pieces[8] == "X") or (self.pieces[2] == "O" and self.pieces[8] == "O")) \
                and self.pieces[5] == " ":
            return 6
        elif ((self.pieces[0] == "X" and self.pieces[2] == "X") or (self.pieces[0] == "O" and self.pieces[2] == "O")) \
                and self.pieces[1] == " ":
            return 2
        elif ((self.pieces[3] == "X" and self.pieces[5] == "X") or (self.pieces[3] == "O" and self.pieces[5] == "O")) \
                and self.pieces[4] == " ":
            return 5
        elif ((self.pieces[6] == "X" and self.pieces[8] == "X") or (self.pieces[6] == "O" and self.pieces[8] == "O")) \
                and self.pieces[7] == " ":
            return 8
        elif ((self.pieces[0] == "X" and self.pieces[8] == "X") or (self.pieces[0] == "O" and self.pieces[8] == "O")) \
                and self.pieces[4] == " ":
            return 5
        elif ((self.pieces[2] == "X" and self.pieces[6] == "X") or (self.pieces[2] == "O" and self.pieces[6] == "O")) \
                and self.pieces[4] == " ":
            return 5
        else:
            return random.randint(1, 9)
