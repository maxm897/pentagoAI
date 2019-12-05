import evaluate
import GamePlay
from copy import copy, deepcopy
import numpy as np
import operator


bestaction = None

def minimax(board, depth, alpha, beta, bestaction, is_top):
    initial_eval = evaluate.evaluate(board)
    if ((initial_eval==-9999999) or (initial_eval==9999999) or (initial_eval==-0.5) or (depth==0)):
        return initial_eval
    else:
        hashes_seen = set()
        val = evaluate.MINVAL
        for x in range(0,6):
            for y in range(0,6):
                if isAvailable(board, x, y):
                    for box in range(1,5):
                        for direction in ["R", "L"]:
                            a = GamePlay.Action(x,y,box,direction)
                            temp = deepcopy(board)
                            new_board = GamePlay.take_action(temp, a, "AI")
                            if isUnique(symmetricBoards(new_board), hashes_seen):
                                hashes_seen.add(hash(str(new_board)))
                                val2 = maximin(new_board, depth-1, alpha, beta, bestaction)
                                if (val2>val):
                                    val=val2
                                    if is_top:
                                        bestaction.x_coordinate=x
                                        bestaction.y_coordinate = y
                                        bestaction.square_index=box
                                        bestaction.direction=direction
                                alpha = max(alpha, val)
                                if alpha >= beta:
                                    return val
        return val




def maximin(board, depth, alpha, beta, bestaction):
    initial_eval = evaluate.evaluate(board)
    if ((initial_eval == -9999999) or (initial_eval == 9999999) or (initial_eval == -0.5) or (depth == 0)):
        return initial_eval
    else:
        hashes_seen = set()
        val = evaluate.MAXVAL
        for x in range(0, 6):
            for y in range(0, 6):
                if (isAvailable(board, x, y)):
                    for box in range(1, 5):
                        for direction in ["R", "L"]:
                            a = GamePlay.Action(x, y, box, direction)
                            temp = deepcopy(board)
                            new_board = GamePlay.take_action(temp, a, "Player")
                            if isUnique(symmetricBoards(new_board), hashes_seen):
                                hashes_seen.add(hash(str(new_board)))
                                val2 = minimax(new_board, depth - 1, alpha, beta, bestaction, False)
                                if (val2 < val):
                                    val = val2
                                beta = min(beta, val)
                                if alpha >= beta:
                                    return val
        return val


def getBestAction(board, depth):
    
    bestaction = findAvailableAction(board)
    print("best action before minimax is " + str(bestaction.x_coordinate) + str(bestaction.y_coordinate))
    temp = deepcopy(board)
    minimax(temp, depth, evaluate.MINVAL, evaluate.MAXVAL, bestaction, True)
    print("best action after minimax is " + str(bestaction.x_coordinate) + str(bestaction.y_coordinate))
    return bestaction

def isAvailable(board, x, y):
    
    if(board[x][y]==0 or board[x][y]==1):

        return False

    return True

def findAvailableAction(board):
    for x in range (0,6):
        for y in range(0,6):
            if isAvailable(board, x, y):
                return GamePlay.Action(x, y, 1, "L")


def symmetricBoards(board):
    output = [board]

    #rotations
    mid_board = np.array(board)
    for i in range(3):
        mid_board = np.rot90(mid_board)
        output.append(mid_board.tolist())

    #horizontal and vertical flips
    mid_board = np.array(board)
    output.append(np.flip(mid_board, axis=0).tolist())
    output.append(np.flip(mid_board, axis=1).tolist())

    #flips across the two diagonals
    output.append(np.flip(np.rot90(mid_board), axis=0).tolist())
    output.append(np.flip(np.rot90(mid_board), axis=1).tolist())

    return output

def isUnique(symmetries, set):
    for board in symmetries:
        if hash(str(board)) in set:
            return False
    return True





                