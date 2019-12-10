from baseconvert import base


def convertBoardToFormat(board):
    # take in board in form of a 36-length ternary tuple, convert to proper form
    bottomLeft = board[:9]
    topLeft = board[9:18]
    bottomRight = board[18:27]
    topRight = board[-9:]

    bottomLeftBinary = convertQuadrantToBinary(bottomLeft)
    topLeftBinary = convertQuadrantToBinary(topLeft)
    bottomRightBinary = convertQuadrantToBinary(bottomRight)
    topRightBinary = convertQuadrantToBinary(topRight)

    concatenatedBinary = topRightBinary + \
        bottomRightBinary + topLeftBinary + bottomLeftBinary

    finalDecimal = convertBinaryToDecimal(concatenatedBinary)
    return finalDecimal


def convertQuadrantToBinary(quad):
    binStart = base(quad, 3, 2)
    zeros = (0,)*(16 - len(binStart))
    final = zeros + binStart
    return final


def convertBinaryToDecimal(binary):
    return base(binary, 2, 10)


def convertFormatToBoard(response):
    pass
