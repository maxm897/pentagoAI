from requests import get
from boardToFormat import convertBoardToFormat, convertFormatToBoard
from random import randint


def takeBoardReturnReponseBoard(board):
    # takes in a board in the form of a 36-length ternary tuple
    # outputs a board in the same format after perfect pentago makes its move
    decimalBoard = convertBoardToFormat(board)
    bestMoveResponse = makeRequest(decimalBoard)

    return convertFormatToBoard(bestMoveResponse)


def makeRequest(state):
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

    newURL = "https://backend.perfect-pentago.net/{}".format(firstMove)

    m = get(url=newURL, params=PARAMS)
    newMovesDict = m.json()

    finalMove = chooseMove(movesDict, 'second')

    return finalMove


def chooseMove(movesDict, move):

    bestState = None
    if move == 'first':
        best = -2
        for state in movesDict:
            if state[-1] == 'm' and movesDict[state] > best:
                bestState = state
                best = movesDict[state]
            if best == 1:
                break
    elif move == 'second':
        best = 2
        for state in movesDict:
            if type(movesDict[state]) == int and int(movesDict[state]) < best:
                bestState = state
                best = movesDict[state]
            elif type(movesDict[state]) == int and int(movesDict[state]) == best and randint(0, 3) == 1:
                bestState = state
                best = movesDict[state]
            if best == -1:
                break

    return bestState
