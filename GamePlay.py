#GamePlay.py
#Richard Greenbaum, Karson Daecher, Max Melamed
"""This module contains the functions needed to support pentago gameplay.

A pentago gameboard is represented by a 6x6 2D array. Each location on the board is initialized to "" and is set
to 0 or 1 when the player or the AI respectively places a marble on that location. Each array in the gameboard 
nested array represents a column of the board. Thus the gameboard can be viewed as the square in the 1st coordinate 
quadrant with x and y coordinates ranging from 0...5. For example, the bottom right location on the gameboard can 
be accessed with the command board[5][0]. The four squares on the board are indexed 1...4 with 1 as bottom left, 2 as
top left, 3 as bottom right, and 4 as top right. """

def new_board():
	"""Returns an empty board"""

	return [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
	[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
def printBoard(board):
	"""prints out the board in a legible format"""
	print("\033[1m   -----------------------------------\033[0m")
	print("5 \033[1m|  \033[0m" + returnMarble(str(board[0][5])) + "  |  " + returnMarble(str(board[1][5])) + "  |  " + returnMarble(str(board[2][5])) +
		  "\033[1m  |  \033[0m" + returnMarble(str(board[3][5])) + "  |  " + returnMarble(str(board[4][5])) + "  |  " + returnMarble(str(board[5][5])) +"\033[1m  |\033[0m")
	print("  \033[1m|\033[0m-----------------\033[1m|\033[0m-----------------\033[1m|\033[0m")
	print("4 \033[1m|  \033[0m" +returnMarble(str(board[0][4])) + "  |  " + returnMarble(str(board[1][4])) + "  |  " + returnMarble(str(board[2][4])) +
		  "\033[1m  |  \033[0m" + returnMarble(str(board[3][4])) + "  |  " + returnMarble(str(board[4][4])) + "  |  " + returnMarble(str(board[5][4]))+"\033[1m  |\033[0m")
	print("  \033[1m|\033[0m-----------------\033[1m|\033[0m-----------------\033[1m|\033[0m")
	print("3 \033[1m|  \033[0m" +returnMarble(str(board[0][3])) + "  |  " + returnMarble(str(board[1][3])) + "  |  " + returnMarble(str(board[2][3])) +
		  "\033[1m  |  \033[0m" + returnMarble(str(board[3][3])) + "  |  " + returnMarble(str(board[4][3])) + "  |  " + returnMarble(str(board[5][3]))+"\033[1m  |\033[0m                  2 | 4                ")
	print("\033[1m  |-----------------|-----------------|\033[0m                  --|--                ")
	print("2 \033[1m|  \033[0m" +returnMarble(str(board[0][2])) + "  |  " + returnMarble(str(board[1][2])) + "  |  " + returnMarble(str(board[2][2])) +
		  "\033[1m  |  \033[0m" + returnMarble(str(board[3][2])) + "  |  " + returnMarble(str(board[4][2])) + "  |  " + returnMarble(str(board[5][2]))+"\033[1m  |\033[0m                  1 | 3                ")
	print("  \033[1m|\033[0m-----------------\033[1m|\033[0m-----------------\033[1m|\033[0m")
	print("1 \033[1m|  \033[0m" + returnMarble(str(board[0][1])) + "  |  " + returnMarble(str(board[1][1])) + "  |  " + returnMarble(str(board[2][1])) +
		  "\033[1m  |  \033[0m" + returnMarble(str(board[3][1])) + "  |  " + returnMarble(str(board[4][1])) + "  |  " + returnMarble(str(board[5][1]))+"\033[1m  |\033[0m")
	print("  \033[1m|\033[0m-----------------\033[1m|\033[0m-----------------\033[1m|\033[0m")
	print("0 \033[1m|  \033[0m" + returnMarble(str(board[0][0])) + "  |  " + returnMarble(str(board[1][0])) + "  |  " + returnMarble(str(board[2][0])) +
		  "\033[1m  |  \033[0m" + returnMarble(str(board[3][0])) + "  |  " + returnMarble(str(board[4][0])) + "  |  " + returnMarble(str(board[5][0]))+"\033[1m  |\033[0m")
	print("\033[1m   -----------------------------------\033[0m")
	print("     0     1     2     3     4     5")
	return

def returnMarble(number):
	"""Returns a string, red X for AI and black X for human player"""
	if (number =="1"):
		return "\033[91mX\033[0m"
	elif (number == "0"):
		return "X"
	else:
		return number
	



def rotate(board, direction, square_index):
	"""Returns a copy of the board with the indicated square rotated 90 degrees in the indicated direction

	Parameter board: a valid pentago board
	Parameter direction: the direction of rotation                        "R" or "L"
	Parameter square_index: the index of the square to be rotated         int 1...4
	"""

	if square_index == 1:
		
		vertical_offset = 0
		horizontal_offset = 0
	if square_index == 2:
		
		vertical_offset = 3
		horizontal_offset = 0
	if square_index == 3:
		
		vertical_offset = 0
		horizontal_offset = 3
	if square_index == 4:
		
		vertical_offset = 3
		horizontal_offset = 3

	if direction == "R":

		temp1 = board[2 + horizontal_offset][1 + vertical_offset]
		temp2 = board[1 + horizontal_offset][0 + vertical_offset]
		board[2 + horizontal_offset][1 + vertical_offset] = board[1 + horizontal_offset][2 + vertical_offset]
		board[1 + horizontal_offset][0 + vertical_offset] = temp1
		temp1 = board[0 + horizontal_offset][1 + vertical_offset]
		board[0 + horizontal_offset][1 + vertical_offset] = temp2
		board[1 + horizontal_offset][2 + vertical_offset] = temp1

		temp1 = board[2 + horizontal_offset][2 + vertical_offset]
		temp2 = board[2 + horizontal_offset][0 + vertical_offset]
		board[2 + horizontal_offset][2 + vertical_offset] = board[0 + horizontal_offset][2 + vertical_offset]
		board[2 + horizontal_offset][0 + vertical_offset] = temp1
		temp1 = board[0 + horizontal_offset][0 + vertical_offset]
		board[0 + horizontal_offset][0 + vertical_offset] = temp2
		board[0 + horizontal_offset][2 + vertical_offset] = temp1

	if direction == "L":

		temp1 = board[0 + horizontal_offset][1 + vertical_offset]
		temp2 = board[1 + horizontal_offset][0 + vertical_offset]
		board[0 + horizontal_offset][1 + vertical_offset] = board[1 + horizontal_offset][2 + vertical_offset]
		board[1 + horizontal_offset][0 + vertical_offset] = temp1
		temp1 = board[2 + horizontal_offset][1 + vertical_offset]
		board[2 + horizontal_offset][1 + vertical_offset] = temp2
		board[1 + horizontal_offset][2 + vertical_offset] = temp1

		temp1 = board[0 + horizontal_offset][2 + vertical_offset]
		temp2 = board[0 + horizontal_offset][0 + vertical_offset]
		board[0 + horizontal_offset][2 + vertical_offset] = board[2 + horizontal_offset][2 + vertical_offset]
		board[0 + horizontal_offset][0 + vertical_offset] = temp1
		temp1 = board[2 + horizontal_offset][0 + vertical_offset]
		board[2 + horizontal_offset][0 + vertical_offset] = temp2
		board[2 + horizontal_offset][2 + vertical_offset] = temp1

	return board 

def take_action(board, action, player):
	"""Takes a given action on a given board for a given player. Returns the new board.

	Parameter board: a valid game board
	Parameter action: an instance of type Action
	Parameter player: either "Player" or "AI"
	"""

	if player == "Player":
		set_value = 0
	else:
		set_value = 1
	temp=board
	temp[action.x_coordinate][action.y_coordinate] = set_value
	return rotate(temp, action.direction, action.square_index)
	

class Action(object):
	"""Each acton is composed of the location on the board for a marble to be placed, a square selection, 
	and the direction that that square should be rotated."""

	def __init__(self, x_coordinate, y_coordinate, square_index, direction):
		"""Creates an instance of class Action

		Parameter x_coordinate: x coordinate of the location for the marble to be placed    int 0...5
		Parameter y_coordinate: y coordinate of the location for the marble to be placed    int 0...5
		Parameter square_index: the index of the square to be rotated                       int 1...4
		Parameter direction: the direction of rotation                                      "R" or "L"
        """

		self.x_coordinate = x_coordinate    
		self.y_coordinate = y_coordinate
		self.square_index = square_index
		self.direction = direction



	def equals(self, action):
		"""method of class Action that determines if an action is equal to another action"""
		
		assert(isinstance(action, Action))
		
		if not(self.x_coordinate==action.x_coordinate):
			return False
		if not(self.y_coordinate==action.y_coordinate):
			return False
		if not(self.square_index==action.square_index):
			return False
		if not(self.direction==action.direction):
			return False
		return True




	

