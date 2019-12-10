from requests import get


def makeRequest(state):
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

    finalMove = chooseMove(movesDict, 'second')

    print(finalMove)
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
            if best == -1:
                break

    return bestState
