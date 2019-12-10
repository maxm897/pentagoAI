from requests import get


def makeRequest(state):
    stringList = list(map(str, state))
    boardString = ''.join(stringList)
    URL = "https://backend.perfect-pentago.net/{}".format(boardString)
    PARAMS = {}
    r = get(url=URL, params=PARAMS)
    movesDict = r.json()
    print(mvoesDict)
    return chooseMove(movesDict)


def chooseMove(movesDict):
    print(movesDict)
    return (list(movesDict))[0]
