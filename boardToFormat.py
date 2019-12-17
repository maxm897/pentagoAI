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
    # take in the response of the perfect pentago API in the format of a decimal
    # number and convert it back to a 36-length ternary tuple

    b = convertDecimalToBinary(response)
    zeros = (0,)*(64 - len(b))
    finalBin = zeros + b
    topRightBinary = finalBin[:16]
    bottomRightBinary = finalBin[16:32]
    topLeftBinary = finalBin[32:48]
    bottomLeftBinary = finalBin[48:]

    topRightFinal = convertBinaryToQuadrant(topRightBinary)
    bottomRightFinal = convertBinaryToQuadrant(bottomRightBinary)
    topLeftFinal = convertBinaryToQuadrant(topLeftBinary)
    bottomLeftFinal = convertBinaryToQuadrant(bottomLeftBinary)

    concatenatedFinal = bottomLeftFinal + \
        topLeftFinal + bottomRightFinal + topRightFinal

    return concatenatedFinal


def convertBinaryToQuadrant(binary):
    quadStart = base(binary, 2, 3)
    zeros = (0,)*(9 - len(quadStart))
    final = zeros + quadStart
    return final


def convertDecimalToBinary(decimal):
    return base(decimal, 10, 2)
