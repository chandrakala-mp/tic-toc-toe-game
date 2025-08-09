def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        try:
            print(f"Waiting for input from Player {current_player}...")
            move = input(f"Player {current_player}, enter your move (row and column 1-3, e.g. 1 3): ")
            print(f"Received input: {move}")
            row, col = map(int, move.strip().split())
            row -= 1
            col -= 1

            if row not in range(3) or col not in range(3):
                print("Row and column must be between 1 and 3.")
                continue

            if board[row][col] != " ":
                print("That cell is already taken. Try again.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break

            if is_full(board):
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"

        except Exception as e:
            print(f"Error: {e}. Please enter input in the form 'row column' (e.g., 2 3)")

if __name__ == "__main__":
    main()
