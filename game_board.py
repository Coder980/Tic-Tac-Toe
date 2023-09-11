class GameBoard:
    def __init__(self):
        self.used_numbers = []
        self.completed_moves = 0
        self.pieces = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.board = f" {self.pieces[0]} | {self.pieces[1]} | {self.pieces[2]}  \n" \
                     "-----------\n" \
                     f" {self.pieces[3]} | {self.pieces[4]} | {self.pieces[5]}  \n" \
                     "-----------\n" \
                     f" {self.pieces[6]} | {self.pieces[7]} | {self.pieces[8]}  \n"

    def update_game_board(self, piece_symbol, piece_number):
        if piece_number == 1:
            self.pieces[0] = piece_symbol
        elif piece_number == 2:
            self.pieces[1] = piece_symbol
        elif piece_number == 3:
            self.pieces[2] = piece_symbol
        elif piece_number == 4:
            self.pieces[3] = piece_symbol
        elif piece_number == 5:
            self.pieces[4] = piece_symbol
        elif piece_number == 6:
            self.pieces[5] = piece_symbol
        elif piece_number == 7:
            self.pieces[6] = piece_symbol
        elif piece_number == 8:
            self.pieces[7] = piece_symbol
        else:
            self.pieces[8] = piece_symbol

        self.board = f"\n {self.pieces[0]} | {self.pieces[1]} | {self.pieces[2]}  \n" \
                     "-----------\n" \
                     f" {self.pieces[3]} | {self.pieces[4]} | {self.pieces[5]}  \n" \
                     "-----------\n" \
                     f" {self.pieces[6]} | {self.pieces[7]} | {self.pieces[8]}  \n"
        print(self.board)

    def get_naughts(self):
        naughts = 0
        for piece in self.pieces:
            if piece == "X":
                naughts += 1
        return naughts

    def get_crosses(self):
        crosses = 0
        for piece in self.pieces:
            if piece == "O":
                crosses += 1
        return crosses

    def play_turn(self, player_piece, player_choice):
        try:
            int(player_choice)
        except ValueError:
            print("\nNot a valid answer.")
            return False
        else:
            player_choice = int(player_choice)
            if 0 < player_choice < 10:
                self.used_numbers.append(player_choice)
                num_count = 0
                for num in self.used_numbers:
                    if num == player_choice:
                        num_count += 1
                if num_count <= 1:
                    self.update_game_board(player_piece, player_choice)
                    self.completed_moves += 1
                    return True
                else:
                    print("\nAlready chosen, pick another number.")
                    return False
            else:
                print("\nOut of Range.")
                return False

    def game_over(self):
        if self.pieces[0] == "X" and self.pieces[1] == "X" and self.pieces[2] == "X":
            print("Player 1 has won!")
            return True
        elif self.pieces[0] == "O" and self.pieces[1] == "O" and self.pieces[2] == "O":
            print("Player 2 has won!")
            return True
        elif self.pieces[3] == "X" and self.pieces[4] == "X" and self.pieces[5] == "X":
            print("Player 1 has won!")
            return True
        elif self.pieces[3] == "O" and self.pieces[4] == "O" and self.pieces[5] == "O":
            print("Player 2 has won!")
            return True
        elif self.pieces[6] == "X" and self.pieces[7] == "X" and self.pieces[8] == "X":
            print("Player 1 has won!")
            return True
        elif self.pieces[6] == "O" and self.pieces[7] == "O" and self.pieces[8] == "O":
            print("Player 2 has won!")
            return True
        elif self.pieces[0] == "X" and self.pieces[3] == "X" and self.pieces[6] == "X":
            print("Player 1 has won!")
            return True
        elif self.pieces[0] == "O" and self.pieces[3] == "O" and self.pieces[6] == "O":
            print("Player 2 has won!")
            return True
        elif self.pieces[1] == "X" and self.pieces[4] == "X" and self.pieces[7] == "X":
            print("Player 1 has won!")
            return True
        elif self.pieces[1] == "O" and self.pieces[4] == "O" and self.pieces[7] == "O":
            print("Player 2 has won!")
            return True
        elif self.pieces[2] == "X" and self.pieces[5] == "X" and self.pieces[8] == "X":
            print("Player 1 has won!")
            return True
        elif self.pieces[2] == "O" and self.pieces[5] == "O" and self.pieces[8] == "O":
            print("Player 2 has won!")
            return True
        elif self.pieces[0] == "X" and self.pieces[4] == "X" and self.pieces[8] == "X":
            print("Player 1 has won!")
            return True
        elif self.pieces[0] == "O" and self.pieces[4] == "O" and self.pieces[8] == "O":
            print("Player 2 has won!")
            return True
        elif self.pieces[2] == "X" and self.pieces[4] == "X" and self.pieces[6] == "X":
            print("Player 1 has won!")
            return True
        elif self.pieces[2] == "O" and self.pieces[4] == "O" and self.pieces[6] == "O":
            print("Player 2 has won!")
            return True
        elif self.completed_moves == 9:
            print("It's a Draw!")
            return True
        else:
            return False
