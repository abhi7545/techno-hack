import random

# Length of the board
SIDE = 3

# Function to show the current board status
def showBoard(board):
	print("\n\n")
	for i in range(SIDE):
		print(f"\t\t\t {board[i][0]} | {board[i][1]} | {board[i][2]}")
		if i != SIDE - 1:
			print("\t\t\t------------")
	print("\n")
	return

# Function to show the instructions
def showInstructions():
	print("\t\t\t Tic-Tac-Toe\n\n")
	print("Choose a cell numbered from 1 to 9 as below and play\n\n")
	print("\t\t\t 1 | 2 | 3 ")
	print("\t\t\t------------")
	print("\t\t\t 4 | 5 | 6 ")
	print("\t\t\t------------")
	print("\t\t\t 7 | 8 | 9 \n\n")
	print("-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n\n")
	return

# Function to initialize the game
def initialise(board, moves):
	random.seed()
	for i in range(SIDE):
		for j in range(SIDE):
			board[i][j] = ' '
	for i in range(SIDE * SIDE):
		moves[i] = i
	random.shuffle(moves)
	return

# Function to declare the winner of the game
def declareWinner(whoseTurn):
	print(f"{PLAYER1 if whoseTurn == PLAYER1 else PLAYER2} has won")
	return

# Function that returns true if any row is crossed with the same player's move
def rowCrossed(board):
	for i in range(SIDE):
		if board[i][0] == board[i][1] == board[i][2] != ' ':
			return True
	return False

# Function that returns true if any column is crossed with the same player's move
def columnCrossed(board):
	for i in range(SIDE):
		if board[0][i] == board[1][i] == board[2][i] != ' ':
			return True
	return False

# Function that returns true if any diagonal is crossed with the same player's move
def diagonalCrossed(board):
	if board[0][0] == board[1][1] == board[2][2] != ' ':
		return True
	if board[0][2] == board[1][1] == board[2][0] != ' ':
		return True
	return False

# Function that returns true if the game is over else it returns False
def gameOver(board):
	return rowCrossed(board) or columnCrossed(board) or diagonalCrossed(board)

# Function to play Tic-Tac-Toe
def playTicTacToe(whoseTurn):
	board = [[' ' for _ in range(SIDE)] for _ in range(SIDE)]
	moves = [i for i in range(SIDE * SIDE)]

	# Initialize the game
	initialise(board, moves)

	# Show instructions before playing
	showInstructions()

	moveIndex = 0
	while not gameOver(board) and moveIndex != SIDE * SIDE:
		if whoseTurn == PLAYER1:
			# Input the desired row and column by player 1 to insert X
			print(f"{PLAYER1} Enter the respective row and column to insert X :")
			r, c = map(int, input().split())
			if 1 <= r <= 3 and 1 <= c <= 3 and board[r - 1] == ' ':
				board[r - 1] = 'X'
			else:
				print("Invalid input. Try again.")
				continue
		else:
			# Input the desired row and column by player 2 to insert O
			print(f"{PLAYER2} Enter the respective row and column to insert O :")
			r, c = map(int, input().split())
			if 1 <= r <= 3 and 1 <= c <= 3 and board[r - 1] == ' ':
				board[r - 1] = 'O'
			else:
				print("Invalid input. Try again.")
				continue

		showBoard(board)
		moveIndex += 1
		whoseTurn = PLAYER2 if whoseTurn == PLAYER1 else PLAYER1

	# If the game has drawn
	if not gameOver(board) and moveIndex == SIDE * SIDE:
		print("It's a draw")
	else:
		# Toggling the user to declare the actual winner
		whoseTurn = PLAYER2 if whoseTurn == PLAYER1 else PLAYER1
		declareWinner(whoseTurn)
	return

# Driver code
PLAYER1 = input("Enter name of first Player: ")
PLAYER2 = input("Enter name of Second Player: ")

# Use current time as seed for random generator
random.seed()

# Let's do a toss
toss = random.randint(0, 1)

# Let us play the game
if toss == 1:
	print(f"Player {PLAYER1} won the toss")
	playTicTacToe(PLAYER1)
else:
	print(f"Player {PLAYER2} won the toss")
	playTicTacToe(PLAYER2)
