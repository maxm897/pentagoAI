import evaluate
import minimax
import GamePlay
import sys
import tkinter

def main():
	print('Welcome to Pentago! The first player to get 5 marbles in a row wins the game. In each turn,',
		'players place a marble in an empty circle and then rotate one of the four primary game squares',
		'90 degrees. A turn is specified by 4 inputs: The x coordinate of the marble location (int 0...5),',
		'the y coordinate of the marble location (int 0...5), the index of the square to be rotated',
		'(int 1...4) and the direstion fo rotation ("R" or "L"). See the following diagrams for reference.',
		'Good luck!',
		'\n\nBoard Layout:\n5 \n4 \n3 \n2 \n1 \n0 1 2 3 4 5 \n\nSquare Index Layout:\n2   4\n1   3\n')

	new_game()

def new_game():
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
	while (game_over==False):
		if turn==0:
			x = input("Please input the x coordinate where you would like to place your marble")

			while (valid(x, 1)==False):
			    x=input("Invalid input, please select a number between 1 and 6")


			y = input("Please input the y coordinate")

			while (valid(y, 1)==False):
				y=input("Invalid input, please select a number between 1 and 6")


			s = input("Please select which square you would like to rotate")
			while (valid(s, 2)==False):
				s=input("invalid input, please enter an integer between 1 and 4")
			
			d = input("please select a direction you would like to rotate the sqaure")
			while (valid(d, 3)==False):
				d = input("invalid input, please enter 'R' or 'L'")
			
			action = GamePlay.Action(int(x)-1, int(y)-1, int(s), d)
			board=GamePlay.take_action(board, action, "Player")
			print("the new board is " + str(board))
			turn=1
		if turn==1:
			
			##minimax.minimax(board, 3, action)
			action=minimax.getBestAction(board, 3)
			board=GamePlay.take_action(board, action, "AI")
			print("the AI has taken action: x=" + str(action.x_coordinate) + ", y=" + str(action.y_coordinate)
				  + ", box=" + str(action.square_index) + ", direction=" + str(action.direction))
			print("the new board is " + str(board))
			turn=0
			


def valid(x, type):
	"""helper function determining if input is valid
	paramter x = the input
	parameter type is the type of input, 1 is a coordinate, 2 is a box, 3 is a direction"""
	assert (type==1 or type ==2 or type==3)
	
	
	if (type==1):
		try:
			if (int(x)<1 or int(x)>6):
				return False
		except ValueError:
			return False
	elif (type==2):
		try:
			if (int(x)<1 or int(x)>4):
				return False
		except ValueError:
			return False
		

	elif (type==3 and x!="R" and x!="L"):
		return False
	

	return True

if __name__ == "__main__":
	main()


