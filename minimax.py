import evaluate
import GamePlay



def minimax(board, depth):
    if (isdone(board) or depth==0):
        return evaluate.evaluate(board)
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



def isdone(board):
    pass

def maximin(board, depth):
    pass