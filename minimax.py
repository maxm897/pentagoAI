import evaluate
import GamePlay
from copy import copy, deepcopy


bestaction = None

def minimax(board, depth, bestaction):
    eval = evaluate.evaluate(board)
    if ((eval==-9999999) or (eval==9999999) or (eval==-0.5) or (depth==0)):
        return eval
    else:
        val = evaluate.MINVAL
<<<<<<< HEAD
        for x in range(0,6):
            for y in range(0,6):
                if isAvailable(board, x, y):
                    for box in range(1,5):
                        for dir in ["R", "L"]:
                            a = GamePlay.Action(x,y,box,dir)
                            val2 = maximin(GamePlay.take_action(board, a, "AI"), depth-1, bestaction)
                            if (val2>val):
                                val=val2
                                bestaction.x_coordinate=x
                                bestaction.y_coordinate = y
                                bestaction.square_index=box
                                bestaction.direction=dir
=======
        for x in range(6):
            for y in range(6):
                for box in range(1,5):
                    for dir in ["R", "L"]:
                        a = GamePlay.Action(x,y,box,dir)
                        val2 = maximin(GamePlay.take_action(board, a, "AI"), depth-1, bestaction)
                        if (val2>val):
                            val=val2
                            bestaction.x_coordinate=x
                            bestaction.y_coordinate = y
                            bestaction.square_index=box
                            bestaction.direction=dir
>>>>>>> refs/remotes/origin/master
        return val




def maximin(board, depth, bestaction):
    eval = evaluate.evaluate(board)
    if ((eval == -9999999) or (eval == 9999999) or (eval == -0.5) or (depth == 0)):
        return eval
    else:
        val = evaluate.MAXVAL
<<<<<<< HEAD
        for x in range(0, 6):
            for y in range(0, 6):
                if (isAvailable(board, x, y)):
                    for box in range(1, 5):
                        for dir in ["R", "L"]:
                            a = GamePlay.Action(x, y, box, dir)
                            val2 = minimax(GamePlay.take_action(board, a, "Player"), depth - 1, bestaction)
                            if (val2 < val):
                                val = val2
=======
        for x in range(6):
            for y in range(6):
                for box in range(1, 5):
                    for dir in ["R", "L"]:
                        a = GamePlay.Action(x, y, box, dir)
                        val2 = minimax(GamePlay.take_action(board, a, "Player"), depth - 1, bestaction)
                        if (val2 < val):
                            val = val2
>>>>>>> refs/remotes/origin/master
        return val


def getBestAction(board, depth):
    bestaction = GamePlay.Action(1,1,1,"L")
    temp = deepcopy(board)
    minimax(temp, depth, bestaction)
    return bestaction

def isAvailable(board, x, y):
    if(board[x][y]==0 or board[x][y]==1):
        return False
    return True