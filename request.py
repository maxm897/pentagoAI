from requests import get
from boardToFormat import convertBoardToFormat, convertFormatToBoard
from random import choice


def takeBoardReturnReponseBoard(board):
    # takes in a board in the form of a 36-length ternary tuple
    # outputs a board in the same format after perfect pentago makes its move
    print(board)
    decimalBoard = convertBoardToFormat(board)
    # print(decimalBoard)
    bestMoveResponse = makeRequest(decimalBoard)
    c = convertFormatToBoard(bestMoveResponse)
    print(c)
    return c


def makeRequest(state):
    print(state)
    # takes in a board state as a decimal number represented as a tuple
    # makes a request to the perfect pentago API
    # returns the best response in the format of a decimal int
    stringList = list(map(str, state))
    boardString = ''.join(stringList)
    URL = "https://backend.perfect-pentago.net/{}".format(boardString)
    PARAMS = {}

    r = get(url=URL, params=PARAMS)
    movesDict = r.json()

    firstMove = chooseMove(movesDict, 'first')
    print(firstMove)

    newURL = "https://backend.perfect-pentago.net/{}".format(firstMove)

    m = get(url=newURL, params=PARAMS)
    newMovesDict = m.json()

    finalMove = chooseMove(newMovesDict, 'second')
    print("final")
    print(finalMove)
    return finalMove


def chooseMove(movesDict, move):

    bestState = None
    if move == 'first':
        best = -2
        bestMoves = []
        for state in movesDict:
            if state[-1] == 'm' and movesDict[state] > best:
                best = movesDict[state]
                bestMoves = [state]
            elif state[-1] == 'm' and movesDict[state] == best:
                best = movesDict[state]
                bestMoves.append(state)

    elif move == 'second':
        best = 2
        bestMoves = []
        for state in movesDict:
            if type(movesDict[state]) == int and int(movesDict[state]) < best and state[-1] != 'm':
                best = movesDict[state]
                bestMoves = [state]
            elif type(movesDict[state]) == int and int(movesDict[state]) == best and state[-1] != 'm':
                best = movesDict[state]
                bestMoves.append(state)
    if bestMoves:
        return choice(bestMoves)
    else:
        raise Exception()
