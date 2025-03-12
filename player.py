def player_move(pos, board):
    row, col = pos[1] // 200, pos[0] // 200
    if board[row, col] == ' ':
        board[row, col] = 'X'
        return row, col
    return None, None
