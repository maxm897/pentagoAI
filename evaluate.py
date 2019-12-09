#AI.py
#Richard Greenbaum, Karson Daecher, Max Melamed

"""This module contains the AI components of the pentago bot"""

#Points for each board condition
CENTER_BONUS = 5
SEQUENCE2_WEAK = 2
SEQUENCE2_STRONG = 3
SEQUENCE3_WEAK = 10
SEQUENCE3_STRONG = 15
SEQUENCE4 = 20
CENTER_SPREAD1 = .05
CENTER_SPREAD2 = .025
MINVAL = -9999999
MAXVAL = 9999999

def evaluate(board):
	"""Returns an float representing the relatve strength of the board. Positive values represent a stronger
	position for the AI and negative values represent a stronger position for the player. A return value of 9999999
	denotes a win for the AI. A return value of -9999999 denotes a win for the Player. A return value of -.005 denotes a tie.

	Its long. Its ugly. But I can't think of any other way to evaluate a pentago board. 

	Parameter board: a valid game board
	"""

	#Weak sequences are sequences spread across different squares
	#Strong sequences are contained on one square
	Player_sequence2_weak = 0
	Player_sequence2_strong = 0
	Player_sequence3_weak = 0
	Player_sequence3_strong = 0
	Player_sequence4 = 0
	Player_sequence5 = 0

	AI_sequence2_weak = 0
	AI_sequence2_strong = 0
	AI_sequence3_weak = 0
	AI_sequence3_strong = 0
	AI_sequence4 = 0
	AI_sequence5 = 0

	#Specialty measures
	Player_cross2_weak = 0
	Player_cross2_strong = 0
	Player_cross3_weak = 0
	Player_cross3_strong = 0
	Player_cross4 = 0

	AI_cross2_weak = 0
	AI_cross2_strong = 0
	AI_cross3_weak = 0
	AI_cross3_strong = 0
	AI_cross4 = 0

	Player_diagonal2_weak = 0
	Player_diagonal2_strong = 0
	Player_diagonal3_weak = 0
	Player_diagonal3_strong = 0
	Player_diagonal4 = 0

	AI_diagonal2_weak = 0
	AI_diagonal2_strong = 0
	AI_diagonal3_weak = 0
	AI_diagonal3_strong = 0
	AI_diagonal4 = 0

	Player_center_spread1 = 0
	Player_center_spread2 = 0

	AI_center_spread1 = 0
	AI_center_spread2 = 0


	#Find runs in every column
	for x in range(6):
		for y in range(6):
			if y == 0:
				current_type = board[x][y]
				run_length = 1
			elif y == 5:
				if board[x][y] == current_type:
					run_length+=1
				if current_type == 0:
					if run_length == 2:
						if x in [1, 4]:
							Player_cross2_strong+=1
						else:
							Player_sequence2_strong+=1
					if run_length == 3:
						if board[x][y] == current_type:
							if x in [1,4]:
								Player_cross3_strong+=1
							else:
								Player_sequence3_strong+=1
						else:
							if x in [1,4]:
								Player_cross3_weak+=1
							else:
								Player_sequence3_weak+=1
					if run_length == 4:
						if x in [1,4]:
							Player_cross4+=1
						else:
							Player_sequence4+=1
					if run_length > 4:
						Player_sequence5+=1
				if current_type == 1:
					if run_length == 2:
						if x in [1,4]:
							AI_cross2_strong+=1
						else:
							AI_sequence2_strong+=1
					if run_length == 3:
						if board[x][y] == current_type:
							if x in [1,4]:
								AI_cross3_strong+=1
							else:
								AI_sequence3_strong+=1
						else:
							if x in [1,4]:
								AI_cross3_weak+=1
							else:
								AI_sequence3_weak+=1
					if run_length == 4:
						if x in [1,4]:
							AI_cross4+=1
						else:	
							AI_sequence4+=1
					if run_length > 4:
						AI_sequence5+=1
			else:
				if board[x][y] == current_type:
					run_length+=1
				else:
					if current_type == 0:
						if run_length == 2:
							if y == 4:
								if x in [1,4]:
									Player_cross2_weak+=1
								else:
									Player_sequence2_weak+=1
							else:
								if x in [1,4]:
									Player_cross2_strong+=1
								else:
									Player_sequence2_strong+=1
						if run_length == 3:
							if y == 3:
								if x in [1,4]:
									Player_cross3_strong+=1
								else:
									Player_sequence3_strong+=1
							else:
								if x in [1,4]:
									Player_cross3_weak+=1
								else:	
									Player_sequence3_weak+=1
						if run_length == 4:
							if x in [1,4]:
								Player_cross4+=1
							else:
								Player_sequence4+=1
						if run_length > 4:
							Player_sequence5+=1
					if current_type == 1:
						if run_length == 2:
							if y == 4:
								if x in [1,4]:
									AI_cross2_weak+=1
								else:
									AI_sequence2_weak+=1
							else:
								if x in [1,4]:
									AI_cross2_strong+=1
								else:
									AI_sequence2_strong+=1
						if run_length == 3:
							if y == 3:
								if x in [1,4]:
									AI_cross3_strong+=1
								else:
									AI_sequence3_strong+=1
							else:
								if x in [1,4]:
									AI_cross3_weak+=1
								else:
									AI_sequence3_weak+=1
						if run_length == 4:
							if x in [1,4]:
								AI_cross4+=1
							else:
								AI_sequence4+=1
						if run_length > 4:
							AI_sequence5+=1

					current_type = board[x][y]
					run_length = 1

	#find runs in every row
	for y in range(6):
		for x in range(6):
			if x == 0:
				current_type = board[x][y]
				run_length = 1
			elif x == 5:
				if board[x][y] == current_type:
					run_length+=1
				if current_type == 0:
					if run_length == 2:
						if y in [1, 4]:
							Player_cross2_strong+=1
						else:
							Player_sequence2_strong+=1
					if run_length == 3:
						if board[x][y] == current_type:
							if y in [1,4]:
								Player_cross3_strong+=1
							else:
								Player_sequence3_strong+=1
						else:
							if y in [1,4]:
								Player_cross3_weak+=1
							else:
								Player_sequence3_weak+=1
					if run_length == 4:
						if y in [1,4]:
							Player_cross4+=1
						else:
							Player_sequence4+=1
					if run_length > 4:
						Player_sequence5+=1
				if current_type == 1:
					if run_length == 2:
						if y in [1,4]:
							AI_cross2_strong+=1
						else:
							AI_sequence2_strong+=1
					if run_length == 3:
						if board[x][y] == current_type:
							if y in [1,4]:
								AI_cross3_strong+=1
							else:
								AI_sequence3_strong+=1
						else:
							if y in [1,4]:
								AI_cross3_weak+=1
							else:
								AI_sequence3_weak+=1
					if run_length == 4:
						if y in [1,4]:
							AI_cross4+=1
						else:	
							AI_sequence4+=1
					if run_length > 4:
						AI_sequence5+=1
			else:
				if board[x][y] == current_type:
					run_length+=1
				else:
					if current_type == 0:
						if run_length == 2:
							if x == 4:
								if y in [1,4]:
									Player_cross2_weak+=1
								else:
									Player_sequence2_weak+=1
							else:
								if y in [1,4]:
									Player_cross2_strong+=1
								else:
									Player_sequence2_strong+=1
						if run_length == 3:
							if x == 3:
								if y in [1,4]:
									Player_cross3_strong+=1
								else:
									Player_sequence3_strong+=1
							else:
								if y in [1,4]:
									Player_cross3_weak+=1
								else:	
									Player_sequence3_weak+=1
						if run_length == 4:
							if y in [1,4]:
								Player_cross4+=1
							else:
								Player_sequence4+=1
						if run_length > 4:
							Player_sequence5+=1
					if current_type == 1:
						if run_length == 2:
							if x == 4:
								if y in [1,4]:
									AI_cross2_weak+=1
								else:
									AI_sequence2_weak+=1
							else:
								if y in [1,4]:
									AI_cross2_strong+=1
								else:
									AI_sequence2_strong+=1
						if run_length == 3:
							if x == 3:
								if y in [1,4]:
									AI_cross3_strong+=1
								else:
									AI_sequence3_strong+=1
							else:
								if y in [1,4]:
									AI_cross3_weak+=1
								else:
									AI_sequence3_weak+=1
						if run_length == 4:
							if y in [1,4]:
								AI_cross4+=1
							else:
								AI_sequence4+=1
						if run_length > 4:
							AI_sequence5+=1

					current_type = board[x][y]
					run_length = 1

	#Find runs in each of the 6 possible game-winning diagonals 
	#Diagonal 1
	x = 1
	y = 0
	while x!=6:
		if x == 1:
			current_type = board[x][y]
			run_length = 1
		elif x == 5:
			if board[x][y] == current_type:
				run_length+=1
			if current_type == 0:
				if run_length == 2:
					if board[x][y] == current_type:
						Player_sequence2_strong+=1
					else:
						Player_sequence2_weak+=1
				if run_length == 3:
					Player_sequence3_weak+=1
				if run_length == 4:
					Player_sequence4+=1
				if run_length > 4:
					Player_sequence5+=1
			if current_type == 1:
				if run_length == 2:
					if board[x][y] == current_type:
						AI_sequence2_strong+=1
					else:
						AI_sequence2_weak+=1
				if run_length == 3:
					AI_sequence3_weak+=1
				if run_length == 4:
					AI_sequence4+=1
				if run_length > 4:
					AI_sequence5+=1
		else:
			if board[x][y] == current_type:
					run_length+=1
			else: 
				if current_type == 0:
					if run_length == 2:
						if x == 3:
							Player_sequence2_strong+=1
						else:
							Player_sequence2_weak+=1
					if run_length == 3:
						Player_sequence3_weak+=1
					if run_length == 4:
						Player_sequence4+=1
					if run_length > 4:
						Player_sequence5+=1
				if current_type == 1:
					if run_length == 2:
						if x == 3:
							AI_sequence2_strong+=1
						else:
							AI_sequence2_weak+=1
					if run_length == 3:
						AI_sequence3_weak+=1
					if run_length == 4:
						AI_sequence4+=1
					if run_length > 4:
						AI_sequence5+=1

				current_type = board[x][y]
				run_length = 1
		x+=1
		y+=1

	#Diagonal 2
	x = 0
	y = 0
	while x != 6:
		if x == 0:
			current_type = board[x][y]
			run_length = 1
		elif x == 5:
			if board[x][y] == current_type:
				run_length+=1
			if current_type == 0:
				if run_length == 2:
					Player_diagonal2_strong+=1
				if run_length == 3:
					if board[x][y] == current_type:
						Player_diagonal3_strong+=1
					else:
						Player_diagonal3_weak+=1
				if run_length == 4:
					Player_diagonal4+=1
				if run_length > 4:
					Player_sequence5+=1
			if current_type == 1:
				if run_length == 2:
					AI_diagonal2_strong+=1
				if run_length == 3:
					if board[x][y] == current_type:
						AI_diagonal3_strong+=1
					else:
						AI_diagonal3_weak+=1
				if run_length == 4:
					AI_diagonal4+=1
				if run_length > 4:
					AI_sequence5+=1
		else:
			if board[x][y] == current_type:
				run_length+=1
			else: 
				if current_type == 0:
					if run_length == 2:
						if x == 4:
							Player_diagonal2_weak+=1
						else:
							Player_diagonal2_strong+=1
					if run_length == 3:
						if x == 3:
							Player_diagonal3_strong+=1
						else:
							Player_diagonal3_weak+=1
					if run_length == 4:
						Player_diagonal4+=1
					if run_length > 4:
						Player_sequence5+=1
				if current_type == 1:
					if run_length == 2:
						if x == 4:
							AI_diagonal2_weak+=1
						else:
							AI_diagonal2_strong+=1
					if run_length == 3:
						if x == 3:
							AI_diagonal3_strong+=1
						else:
							AI_diagonal3_weak+=1
					if run_length == 4:
						AI_diagonal4+=1

					if run_length > 4:
						AI_sequence5+=1
				current_type = board[x][y]
				run_length = 1
		x+=1
		y+=1

	#Diagonal 3
	x = 0
	y = 1
	while x != 5:
		if x == 0:
			current_type = board[x][y]
			run_length = 1
		elif x == 4:
			if board[x][y] == current_type:
				run_length+=1
			if current_type == 0:
				if run_length == 2:
					if board[x][y] == current_type:
						Player_sequence2_strong+=1
					else:
						Player_sequence2_weak+=1
				if run_length == 3:
					Player_sequence3_weak+=1
				if run_length == 4:
					Player_sequence4+=1
				if run_length > 4:
					Player_sequence5+=1
			if current_type == 1:
				if run_length == 2:
					if board[x][y] == current_type:
						AI_sequence2_strong+=1
					else:
						AI_sequence2_weak+=1
				if run_length == 3:
					AI_sequence3_weak+=1
				if run_length == 4:
					AI_sequence4+=1
				if run_length > 4:
					AI_sequence5+=1
		else:
			if board[x][y] == current_type:
				run_length+=1
			else: 
				if current_type == 0:
					if run_length == 2:
						if x == 2:
							Player_sequence2_strong+=1
						else:
							Player_sequence2_weak+=1
					if run_length == 3:
						Player_sequence3_weak+=1
					if run_length == 4:
						Player_sequence4+=1
					if run_length > 4:
						Player_sequence5+=1
				if current_type == 1:
					if run_length == 2:
						if x == 2:
							AI_sequence2_strong+=1
						else:
							AI_sequence2_weak+=1
					if run_length == 3:
						AI_sequence3_weak+=1
					if run_length == 4:
						AI_sequence4+=1
					if run_length > 4:
						AI_sequence5+=1
				current_type = board[x][y]
				run_length = 1
		x+=1
		y+=1 

	#Diagonal 4
	x = 0
	y = 4
	while x != 5:
		if x == 0:
			current_type = board[x][y]
			run_length = 1
		elif x == 4:
			if board[x][y] == current_type:
				run_length+=1
			if current_type == 0:
				if run_length == 2:
					if board[x][y] == current_type:
						Player_sequence2_strong+=1
					else:
						Player_sequence2_weak+=1
				if run_length == 3:
					Player_sequence3_weak+=1
				if run_length == 4:
					Player_sequence4+=1
				if run_length > 4:
					Player_sequence5+=1
			if current_type == 1:
				if run_length == 2:
					if board[x][y] == current_type:
						AI_sequence2_strong+=1
					else:
						AI_sequence2_weak+=1
				if run_length == 3:
					AI_sequence3_weak+=1
				if run_length == 4:
					AI_sequence4+=1
				if run_length > 4:
					AI_sequence5+=1
		else:
			if board[x][y] == current_type:
				run_length+=1
			else: 
				if current_type == 0:
					if run_length == 2:
						if x == 2:
							Player_sequence2_strong+=1
						else:
							Player_sequence2_weak+=1
					if run_length == 3:
						Player_sequence3_weak+=1

					if run_length == 4:
						Player_sequence4+=1

					if run_length > 4:
						Player_sequence5+=1
				if current_type == 1:
					if run_length == 2:
						if x == 2:
							AI_sequence2_strong+=1
						else:
							AI_sequence2_weak+=1
					if run_length == 3:
						AI_sequence3_weak+=1
					if run_length == 4:
						AI_sequence4+=1
					if run_length > 4:
						AI_sequence5+=1
				current_type = board[x][y]
				run_length = 1
		x+=1
		y-=1

	#Diagonal 5
	x = 0
	y = 5
	while x != 6:
		if x == 0:
			current_type = board[x][y]
			run_length = 1
		elif x == 5:
			if board[x][y] == current_type:
				run_length+=1
			if current_type == 0:
				if run_length == 2:
					Player_diagonal2_strong+=1
				if run_length == 3:
					if board[x][y] == current_type:
						Player_diagonal3_strong+=1
					else:
						Player_diagonal3_weak+=1
				if run_length == 4:
					Player_diagonal4+=1
				if run_length > 4:
					Player_sequence5+=1
			if current_type == 1:
				if run_length == 2:
					AI_diagonal2_strong+=1
				if run_length == 3:
					if board[x][y] == current_type:
						AI_diagonal3_strong+=1
					else:
						AI_diagonal3_weak+-1
				if run_length == 4:
					AI_diagonal4+=1
				if run_length > 4:
					AI_sequence5+=1
		else:
			if board[x][y] == current_type:
				run_length+=1
			else: 
				if current_type == 0:
					if run_length == 2:
						if x == 4:
							Player_diagonal2_weak+=1
						else:
							Player_diagonal2_strong+=1
					if run_length == 3:
						if x == 3:
							Player_diagonal3_strong+=1
						else:
							Player_diagonal3_weak+=1
					if run_length == 4:
						Player_diagonal4+=1
					if run_length > 4:
						Player_sequence5+=1
				if current_type == 1:
					if run_length == 2:
						if x == 4:
							AI_diagonal2_weak+=1
						else:
							AI_diagonal2_strong+=1
					if run_length == 3:
						if x == 3:
							AI_diagonal3_strong+=1
						else:
							AI_diagonal3_weak+=1
					if run_length == 4:
						AI_diagonal4+=1
					if run_length > 4:
						AI_sequence5+=1
				current_type = board[x][y]
				run_length = 1
		x+=1
		y-=1

	#Diagonal 6
	x = 1
	y = 5
	while x != 6:
		if x == 1:
			current_type = board[x][y]
			run_length = 1
		elif x == 5:
			if board[x][y] == current_type:
				run_length+=1
			if current_type == 0:
				if run_length == 2:
					if board[x][y] == current_type:
						Player_sequence2_strong+=1
					else:
						Player_sequence2_weak+=1
				if run_length == 3:
					Player_sequence3_weak+=1
				if run_length == 4:
					Player_sequence4+=1

				if run_length > 4:
					Player_sequence5+=1
			if current_type == 1:
				if run_length == 2:
					if board[x][y] == current_type:
						AI_sequence2_strong+=1
					else:
						AI_sequence2_weak+=1
				if run_length == 3:
					AI_sequence3_weak+=1
				if run_length == 4:
					AI_sequence4+=1
				if run_length > 4:
					AI_sequence5+=1
		else:
			if board[x][y] == current_type:
				run_length+=1
			else: 
				if current_type == 0:
					if run_length == 2:
						if x == 3:
							Player_sequence2_strong+=1
						else:
							Player_sequence2_weak+=1
					if run_length == 3:
						Player_sequence3_weak+=1
					if run_length == 4:
						Player_sequence4+=1
					if run_length > 4:
						Player_sequence5+=1
				if current_type == 1:
					if run_length == 2:
						if x == 3:
							AI_sequence2_strong+=1
						else:
							AI_sequence2_weak+=1
					if run_length == 3:
						AI_sequence3_weak+=1

					if run_length == 4:
						AI_sequence4+=1
					if run_length > 4:
						AI_sequence5+=1
				current_type = board[x][y]
				run_length = 1
		x+=1
		y-=1


	if AI_sequence5 > 0 and Player_sequence5 > 0:
		return -.005
	if AI_sequence5 > 0:
		return 9999999
	if Player_sequence5 > 0:
		return -9999999

	#Determine how many center spots are held by each player
	Player_centers = 0
	AI_centers = 0
	if board[1][1] == 0:
		Player_centers+=1
	if board[1][1] == 1:
		AI_centers+=1
	if board[1][4] == 0:
		Player_centers+=1
	if board[1][4] == 1:
		AI_centers+=1
	if board[4][1] == 0:
		Player_centers+=1
	if board[4][1] == 1:
		AI_centers+=1
	if board[4][4] == 0:
		Player_centers+=1
	if board[4][4] == 1:
		AI_centers+=1

	# determine center spread for each player
	for x in range(6):
		for y in range(6):
			if board[x][y] == 1:
				if center_spread(x, y) == 1:
					AI_center_spread1 += 1
				if center_spread(x, y) == 2:
					AI_center_spread2 += 1
			if board[x][y] == 0:
				if center_spread(x, y) == 1:
					Player_center_spread1 += 1
				if center_spread(x, y) == 2:
					Player_center_spread2 += 1



	Player_score = Player_sequence2_weak*SEQUENCE2_WEAK + Player_sequence2_strong*SEQUENCE2_STRONG + \
		Player_sequence3_weak*SEQUENCE3_WEAK + Player_sequence3_strong*SEQUENCE3_STRONG + \
		Player_sequence4*SEQUENCE4 + Player_centers*CENTER_BONUS + Player_center_spread1*CENTER_SPREAD1 + \
		Player_center_spread2*CENTER_SPREAD2
	AI_score = AI_sequence2_weak*SEQUENCE2_WEAK + AI_sequence2_strong*SEQUENCE2_STRONG + \
		AI_sequence3_weak*SEQUENCE3_WEAK + AI_sequence3_strong*SEQUENCE3_STRONG + \
		AI_sequence4*SEQUENCE4 + AI_centers*CENTER_BONUS + AI_center_spread1*CENTER_SPREAD1 + \
		AI_center_spread2*CENTER_SPREAD2

	#Add diagonal scores
	Player_diagonal = ((board[1][1] == 0 and board[4][4] == 0) or (board[1][4] == 0 and board[4][1] == 0))
	AI_diagonal = ((board[1][1] == 1 and board[4][4] == 1) or (board[1][4] == 1 and board[4][1] == 1))

	if Player_diagonal:
		Player_score += Player_diagonal2_weak*SEQUENCE2_WEAK + Player_diagonal2_strong*SEQUENCE2_STRONG + \
		Player_diagonal3_weak*SEQUENCE3_WEAK + Player_diagonal3_strong*SEQUENCE3_STRONG + \
		Player_diagonal4*SEQUENCE4
	if AI_diagonal:
		AI_score += AI_diagonal2_weak*SEQUENCE2_WEAK + AI_diagonal2_strong*SEQUENCE2_STRONG + \
		AI_diagonal3_weak*SEQUENCE3_WEAK + AI_diagonal3_strong*SEQUENCE3_STRONG + \
		AI_diagonal4*SEQUENCE4

	#Add cross scores
	Player_cross = (board[1][1]==0 and board[4][1]==0) or (board[4][1]==0 and board[4][4]==0) or (board[4][4]==0 and board[1][4]==0) or (board[1][4]==0 and board[1][1]==0)
	AI_cross = (board[1][1]==1 and board[4][1]==1) or (board[4][1]==1 and board[4][4]==1) or (board[4][4]==1 and board[1][4]==1) or (board[1][4]==1 and board[1][1]==1)

	if Player_cross:
		Player_score += Player_cross2_weak*SEQUENCE2_WEAK + Player_cross2_strong*SEQUENCE2_STRONG + \
		Player_cross3_weak*SEQUENCE3_WEAK + Player_cross3_strong*SEQUENCE3_STRONG + \
		Player_cross4*SEQUENCE4

	if AI_cross:
		AI_score += AI_cross2_weak*SEQUENCE2_WEAK + AI_cross2_strong*SEQUENCE2_STRONG + \
		AI_cross3_weak*SEQUENCE3_WEAK + AI_cross3_strong*SEQUENCE3_STRONG + \
		AI_cross4*SEQUENCE4



	return AI_score - Player_score


def center_spread(x, y):
	if x in [0, 5] or y in [0, 5]:
		return -1
	if x in [1, 4] or y in [1, 4]:
		return 2
	return 1 


