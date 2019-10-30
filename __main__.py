import evaluate
import minimax
import GamePlay
import tkinter


def main():
    print('\n\033[1mWelcome to Pentago!\x1b[0m',
          '\nThe first player to get 5 marbles in a row wins the game. In each turn,',
          'players place a marble in an empty circle and then rotate one of the four primary game squares',
          '90 degrees. A turn is specified by 4 inputs:',
          '\n > The x coordinate of the marble location [int 0...5]',
          '\n > The y coordinate of the marble location [int 0...5]',
          '\n > The index of the square to be rotated [int 1...4]',
          '\n > The direction of rotation ["r" or "l"]',
          '\nSee the following diagrams for reference. Good luck!',
          '\n\nBoard Layout:\n5 \n4 \n3 \n2 \n1 \n0 \n 0 1 2 3 4 5 \n\nSquare Index Layout:\n2   4\n1   3\n')
    new_game()


def new_game():
    depth = input("To what depth would you like the AI to search? ")
    while (valid(depth, 4) == False):
        depth = input("invalid depth, please input a non-negative integer ")
    turn = input('Would you like to go first? (y/n) ')
    while turn != 'y' and turn != 'n':
        print('You have entered an invalid input. Type either y or n and then press enter')
        turn = input('Would you like to go first? (y/n) ')
    if turn == 'y':
        turn = 0
    if turn == 'n':
        turn = 1
    board = GamePlay.new_board()

    game_over = False
    while not game_over:
        if turn == 0:
            x = input(
                "Please input the x coordinate where you would like to place your marble ")
            while (valid(x, 1) == False):
                x = input(
                    "Invalid input, please select a number between 0 and 5 ")
            y = input("Please input the y coordinate ")
            while (valid(y, 1) == False):
                y = input(
                    "Invalid input, please select a number between 0 and 5 ")
            while not(minimax.isAvailable(board, int(x), int(y))):
                print(
                    "There is already a marble on the location you selected. Please choose another one")
                x = input(
                    "Please input the x coordinate where you would like to place your marble ")
                while (valid(x, 1) == False):
                    x = input(
                        "Invalid input, please select a number between 0 and 5 ")
                y = input("Please input the y coordinate ")
                while (valid(y, 1) == False):
                    y = input(
                        "Invalid input, please select a number between 0 and 5 ")

            s = input(
                "Please input the index of the square you would like to rotate ")
            while (valid(s, 2) == False):
                s = input(
                    "Invalid input, please enter an integer between 1 and 4 ")

            d = input(
                "Please input the direction you would like to rotate the sqaure ")
            while (valid(d, 3) == False):
                d = input("Invalid input, please enter R or L ")

            action = GamePlay.Action(int(x), int(y), int(s), d)
            board = GamePlay.take_action(board, action, "Player")
            print("The new board is:")
            GamePlay.printBoard(board)
            turn = 1
        else:

            ##minimax.minimax(board, 3, action)

            action = minimax.getBestAction(board, int(depth))
            board = GamePlay.take_action(board, action, "AI")
            print("The AI has taken action: x=" + str(action.x_coordinate) + ", y=" + str(action.y_coordinate)
                  + ", box=" + str(action.square_index) + ", direction=" + str(action.direction))
            print("The new board is: ")
            GamePlay.printBoard(board)
            turn = 0

        if evaluate.evaluate(board) in [9999999, -9999999, -.5]:
            final_score = evaluate.evaluate(board)
            game_over = True
        board_full = True
        for x in range(6):
            for y in range(6):
                if board[x][y] == " ":
                    board_full = False
        if board_full:
            game_over = True
            final_score = -.6

    if final_score == 9999999:
        print("Game over, the AI has won")
    if final_score == -9999999:
        print("Congratulations! You won!")
    if final_score == -.5:
        print("Its a tie!")
    if final_score == -.6:
        print("The board is full, its a tie!")
    again = input('Would you like to play again? (y/n) ')
    while again != 'y' and again != 'n':
        print('You have entered an invalid input. Type either y or n and then press enter')
        again = input('Would you like to play again? (y/n) ')
    if again == 'y':
        new_game()


def valid(x, type):
	"""helper function determining if input is valid
	paramter x = the input
	parameter type is the type of input, 1 is a coordinate, 2 is a box, 3 is a direction, 4 is a depth level	"""
	assert (type in [1,2,3,4])
	
	
	if (type==1):
		try:
			if (int(x)<0 or int(x)>5):
				return False
		except ValueError:
			return False
	elif (type==2):
		try:
			if (int(x)<1 or int(x)>4):
				return False
		except ValueError:
			return False
		

	elif (type==3 and x not in ["R", "r", "L", "l"]):
		return False
	
	elif (type==4):
		try:
			if (int(x)<0):
				return False
		except ValueError:
			return False
		

	return True
    


if __name__ == "__main__":
    main()
