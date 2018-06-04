import evaluate
import GamePlay


bestaction = None

def minimax(board, depth):
    eval = evaluate.evaluate(board)
    if ((eval==-9999999) or (eval==9999999) or (eval==-0.5) or (depth==0)):
        return eval
    else:
        val = evaluate.MINVAL
        for x in range(1,7):
            for y in range(1,7):
                for box in range(1,5):
                    for dir in ["R", "L"]:
                        a = GamePlay.Action(x,y,box,dir)
                        val2 = maximin(GamePlay.take_action(board, a, "AI"), depth-1)
                        if (val2>val):
                            val=val2
                            bestaction = a
        return val




def maximin(board, depth):
    eval = evaluate.evaluate(board)
    if ((eval == -9999999) or (eval == 9999999) or (eval == -0.5) or (depth == 0)):
        return eval
    else:
        val = evaluate.MAXVAL
        for x in range(1, 7):
            for y in range(1, 7):
                for box in range(1, 5):
                    for dir in ["R", "L"]:
                        a = GamePlay.Action(x, y, box, dir)
                        val2 = minimax(GamePlay.take_action(board, a, "Player"), depth - 1)
                        if (val2 < val):
                            val = val2
        return val


def getBestAction():
    return bestaction