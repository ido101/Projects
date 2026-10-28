def print_board(pieces):
    print(f"""-------------
| {board_pieces[0]} | {board_pieces[1]} | {board_pieces[2]} |
| {board_pieces[3]} | {board_pieces[4]} | {board_pieces[5]} |
| {board_pieces[6]} | {board_pieces[7]} | {board_pieces[8]} |
-------------""")

print(3//3)
def check_game_winner(sign):
    if ((board_pieces[0] == sign and board_pieces[1] == sign and board_pieces[2] == sign) or (
            board_pieces[0] == sign and board_pieces[3] == sign and board_pieces[6] == sign) or (
            board_pieces[1] == sign and board_pieces[4] == sign and board_pieces[7] == sign) or (
            board_pieces[2] == sign and board_pieces[5] == sign and board_pieces[8] == sign)
            or (board_pieces[3] == sign and board_pieces[4] == sign and board_pieces[5] == sign) or
            (board_pieces[6] == sign and board_pieces[7] == sign and board_pieces[8] == sign)
            or (board_pieces[0] == sign and board_pieces[4] == sign and board_pieces[8] == sign)
            or (board_pieces[2] == sign and board_pieces[4] == sign and board_pieces[6] == sign)):
        return True
    return False


game_winner = "Tie!"
round_num = 0
board_pieces = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
game_ended = False
turn = "X"
while not game_ended and round_num != 9:
    print_board(board_pieces)
    board_piece = input(f"Its {turn}'s turn.\nwhere would you want to place it?\n").strip()
    while True:
        if board_piece not in board_pieces:
            board_piece = input("Please enter a valid number!\n").strip()
            continue
        break
    board_pieces[int(board_piece) - 1] = turn
    round_num += 1
    if check_game_winner("X"):
        game_ended = True
        game_winner = "X won!"
    elif check_game_winner("O"):
        game_ended = True
        game_winner = "O won!"
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
print_board(board_pieces)
print(f"Game Ended! {game_winner}")
