import evaluate
import minimax
import GamePlay
import tkinter
import boardTernaryConversion
import request


def perfectPlay():
  # set up new game
    board = GamePlay.new_board()
    depth = input("To what depth would you like the AI to search? ")
    while (valid(depth, 4) == False):
        depth = input("invalid depth, please input a non-negative integer ")
    game_over = False
    AI_turn = True

    while not game_over:
        if AI_turn:
            action = minimax.getBestAction(board, int(depth))
            board = GamePlay.take_action(board, action, "AI")
            print("The AI has taken action: x=" + str(action.x_coordinate) + ", y=" + str(action.y_coordinate)
                  + ", box=" + str(action.square_index) + ", direction=" + str(action.direction))
            print("The new board is: ")
            GamePlay.printBoard(board)

        else:
            ternaryBoard = boardTernaryConversion.boardConvertToTernary(board)

            perfectTernaryBoard = request.takeBoardReturnReponseBoard(
                ternaryBoard)

            board = boardTernaryConversion.ternaryConvertToBoard(
                perfectTernaryBoard)

            print("The perfect Pentago bot has taken action:")
            print("The new board is: ")

            GamePlay.printBoard(board)

        if evaluate.evaluate(board) in [9999999, -9999999, -.005]:
            final_score = evaluate.evaluate(board)
            game_over = True
        board_full = True
        for x in range(6):
            for y in range(6):
                if board[x][y] == " ":
                    board_full = False
        if board_full:
            game_over = True
            final_score = -.006

        AI_turn = not AI_turn

    if final_score == 9999999:
        print("Game over, the AI has won")
    if final_score == -9999999:
        print(":( the perfect pentago bot won)")
    if final_score == -.005:
        print("Its a tie!")
    if final_score == -.006:
        print("The board is full, its a tie!")
    again = input('Would you like to play again? (y/n) ')
    while again != 'y' and again != 'n':
        print('You have entered an invalid input. Type either y or n and then press enter')
        again = input('Would you like to play again? (y/n) ')
    if again == 'y':
        perfectPlay()


def valid(x, type):
    """helper function determining if input is valid
    paramter x = the input
    parameter type is the type of input, 1 is a coordinate, 2 is a box, 3 is a direction, 4 is a depth level    """
    assert (type in [1, 2, 3, 4])

    if (type == 1):
        try:
            if (int(x) < 0 or int(x) > 5):
                return False
        except ValueError:
            return False
    elif (type == 2):
        try:
            if (int(x) < 1 or int(x) > 4):
                return False
        except ValueError:
            return False

    elif (type == 3 and x != "R" and x != "L"):
        return False

    elif (type == 4):
        try:
            if (int(x) < 0):
                return False
        except ValueError:
            return False

    return True


if __name__ == "__main__":
    perfectPlay()
