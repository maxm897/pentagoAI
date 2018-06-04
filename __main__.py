import evaluate
import minimax
import GamePlay
import sys

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
	while first != 'y' and first != 'n':
		print('You have entered an invalid input. Type either y or n and then press enter')
		first = input('Would you like to go first? (y/n) ')
	if turn == 'y':
		turn = 0
	if turn == 'n':
		turn = 1
	board = GamePlay.new_board()

	game_over = false
	while !game_over:
		





if __name__ == "__main__":
	main()


