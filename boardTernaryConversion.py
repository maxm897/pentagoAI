def binToTern(digit):
    if digit == "" or digit == " ":
        return 0
    if digit == 0:
        return 1
    if digit == 1:
        return 2


def boardConvertToTernary(board):
    """takes in a game state in the format of a 6 x 6 array and converts it
        to a ternary 36-length tuple where the first 9 bits are the bottom left
        quadrant, second 9 bits are top left, 3rd 9 are bottom right, and last 9
        are top right
        in the output, 1 corresponds to black and 2 to white and 0 to blank"""

    bottomLeft = (binToTern(board[2][2]), binToTern(board[2][1]), binToTern(
        board[2][0]), binToTern(board[1][2]), binToTern(board[1][1]), binToTern(
        board[1][0]), binToTern(board[0][2]), binToTern(board[0][1]), binToTern(board[0][0]))

    topLeft = (binToTern(board[2][5]), binToTern(board[2][4]), binToTern(
        board[2][3]), binToTern(board[1][5]), binToTern(board[1][4]), binToTern(
        board[1][3]), binToTern(board[0][5]), binToTern(board[0][4]), binToTern(board[0][3]))

    bottomRight = (binToTern(board[5][2]), binToTern(board[5][1]), binToTern(
        board[5][0]), binToTern(board[4][2]), binToTern(board[4][1]), binToTern(
        board[4][0]), binToTern(board[3][2]), binToTern(board[3][1]), binToTern(board[3][0]))

    topRight = (binToTern(board[5][5]), binToTern(board[5][4]), binToTern(
        board[5][3]), binToTern(board[4][5]), binToTern(board[4][4]), binToTern(
        board[4][3]), binToTern(board[3][5]), binToTern(board[3][4]), binToTern(board[3][3]))

    return bottomLeft + topLeft + bottomRight + topRight


def ternToBin(col):
    result = []
    for x in col:
        if x == 0:
            result.append(" ")
        if x == 1:
            result.append(0)
        if x == 2:
            result.append(1)
    return result


def ternaryConvertToBoard(tuple):
    """do the opposite of boardConvertToTernary"""

    bottomLeft = tuple[0:9]
    print(bottomLeft)
    topLeft = tuple[9:18]
    print(topLeft)
    bottomRight = tuple[18:27]
    print(bottomRight)
    topRight = tuple[27:]
    print(topRight)

    col1 = ternToBin([bottomLeft[8], bottomLeft[7],
                      bottomLeft[6], topLeft[8], topLeft[7], topLeft[6]])

    col2 = ternToBin([bottomLeft[5], bottomLeft[4],
                      bottomLeft[3], topLeft[5], topLeft[4], topLeft[3]])

    col3 = ternToBin([bottomLeft[2], bottomLeft[1],
                      bottomLeft[0], topLeft[2], topLeft[1], topLeft[0]])

    col4 = ternToBin([bottomRight[8], bottomRight[7],
                      bottomRight[6], topRight[8], topRight[7], topRight[6]])

    col5 = ternToBin([bottomRight[5], bottomRight[4],
                      bottomRight[3], topRight[5], topRight[4], topRight[3]])

    col6 = ternToBin([bottomRight[2], bottomRight[1],
                      bottomRight[0], topRight[2], topRight[1], topRight[0]])

    return [col1, col2, col3, col4, col5, col6]
