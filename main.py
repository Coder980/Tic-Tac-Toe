from player1 import Player1
from player2 import Player2
from ai import AI
from game_board import GameBoard


def start_game(player_1, player_2, board):
    print(board)
    print(f"Player 1 starts with the {player_1.piece} pieces ")
    print(f"Player 2 starts with the {player_2.piece} pieces ")


player1 = Player1()
player2 = AI()
game_board = GameBoard()
start_game(player1, player2, game_board.board)

game_on = True

while game_on:
    naughts = game_board.get_naughts()
    crosses = game_board.get_crosses()

    if naughts <= crosses:
        player1_choice = player1.turn()
        valid_pick = game_board.play_turn(player1.piece, player1_choice)
        if not valid_pick:
            continue

    game_over = game_board.game_over()
    if game_over:
        game_on = False
        break

    if crosses <= naughts:
        player2_choice = player2.turn(game_board.pieces)
        valid_pick = game_board.play_turn(player2.piece, player2_choice)
        if not valid_pick:
            continue

    game_over = game_board.game_over()
    if game_over:
        game_on = False
        break
