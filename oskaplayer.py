import OskaBoard


# Oskaplayer highest level function. Calls minimax on a single board and returns best move.
# 
# Inputs: An OskaBoard, a character representing the moving player, the depth minimax should search to
# 
# Return: the best board found 
def oskaplayer(inBoard, player, depth):
    if not (player == 'w' or player == 'b'):
        print('Invalid player input, aborting.')
        return None

    board = OskaBoard.OskaBoard(inBoard, player)

    output = findbestmove(board, depth)

    minimaxVal = output[1]

    bestMove = output[0]

    if bestMove.wWin() and bestMove.bWin():
        if len(bestMove.bPieces) > len(bestMove.wPieces):
            print('Black wins!')
        elif len(bestMove.bPieces) < len(bestMove.wPieces):
            print('White wins!')
        else:
            print('Draw!')
    elif bestMove.wWin():
        print('White wins!')
    elif bestMove.bWin():
        print('Black wins!')
    else:
        stalemate = True
        for piece in bestMove.wPieces:
            index = bestMove.wPieces.index(piece)
            if bestMove.prep_move_data(piece, index, 'w', bestMove.can_move) > 0:
                stalemate = False
                break
        for piece in bestMove.bPieces:
            index = bestMove.bPieces.index(piece)
            if bestMove.prep_move_data(piece, index, 'b', bestMove.can_move) > 0:
                stalemate = False
                break
        if stalemate:
            print('Draw!')
    
    print('Board Value:', minimaxVal)

    return bestMove.board



# Required move-generation function. (OUTDATED)
# 
# Inputs: Oska board of any length as list, moving player's turn
# 
# Return: List of boards that can be reached from current board in a single move  
def movegen(inBoard, playerTurn):
    Board = OskaBoard.OskaBoard(inBoard, playerTurn)
    return Board.generatechildren()



# Prompts player to move a piece manually. Used in pvp or pvai.
# 
# Inputs: OskaBoard
# 
# Return: new OskaBoard after piece move 
def movepiece(inBoard):
    print('Decide which piece you want to move.')
    startRow = int(input('Starting row:'))
    startCol = int(input('Starting col:'))
    direction = input('Dir:')

    newBoard = inBoard.movepiece(startRow, startCol, direction)
    return newBoard[0]



# Finds the best possible move for a given player (according to evaluate_board).
# 
# Inputs: an OskaBoard, search depth, alpha value, beta value, whether or not the function is maxing or not (boolean)
# 
# Return: tuple: (new board, board's minimax val) 
def minimax(board, depth, alpha, beta, maxing):
    if depth == 0 or board.gameover():
        return (board, board.evaluate_board())
    
    bestBoard = None

    if maxing:
        maxVal = -999999999999
        for child in board.generatechildren():
            curVal = minimax(child, depth - 1, alpha, beta, False)
            if curVal[1] > maxVal:
                maxVal = curVal[1]
                bestBoard = child

            if maxVal > alpha:
                alpha = maxVal
            if beta <= alpha:
                break


        return (bestBoard, maxVal)

    else:
        minVal = 9999999999999
        for child in board.generatechildren():
            curVal = minimax(child, depth - 1, alpha, beta, True)
            if curVal[1] < minVal:
                minVal = curVal[1]
                bestBoard = child

            if minVal < beta:
                beta = minVal
            if beta <= alpha:
                break
        return (bestBoard, minVal)



# Runs minimax algorithm at given depthfor player whose turn it is.
# 
# Inputs: an OskaBoard, a depth for minimax to run
# 
# Return: tuple: (new board, board's minimax val) 
def findbestmove(board, depth):
    if board.playerTurn == 'w':
        return minimax(board, depth, -9999999999999, 9999999999999, True)
    else:
        return minimax(board, depth, -9999999999999, 9999999999999, False)



# Lets a player play against ai, for testing.
# 
# Inputs: None
# 
# Return: None 
def playervsai():
    color = input('Black or White? b/w')
    newBoard = OskaBoard.OskaBoard(['wwwww','----','---','--','---','----','bbbbb'], 'w')



    turnsTaken = 0
    lastBoard = doubleLastBoard = None

    while not newBoard.gameover():
        doubleLastBoard = lastBoard
        lastBoard = newBoard
        turnsTaken += 1
        newBoard.printBoard()
        if newBoard.playerTurn == color:
            print('player move:')
            newBoard = movepiece(newBoard)
            print('board val:', newBoard.evaluate_board())
        else:
            print('opponents move:')
            output = findbestmove(newBoard, 6)
            print('minimax val:', output[1])
            
            newBoard = output[0]
            print('board val:', newBoard.evaluate_board())

        if doubleLastBoard == lastBoard == newBoard:
            break

    newBoard.printBoard()

    

    if newBoard.bWin():
        print('Black wins!')
    elif newBoard.wWin():
        print('White wins!')
    else:
        print('Draw!')

    print('Turns taken:', turnsTaken)



# Lets an ai play against itself with a preset board, for testing.
# 
# Inputs: None
# 
# Return: None 
def aivsai():
    newBoard = OskaBoard.OskaBoard(['wwwww','----','---','--','---','----','bbbbb'], 'w')

    # Test a draw
    #newBoard = OskaBoard.OskaBoard(['------','-----','----','www','ww','bbb','bbbb','-----','------'], 'w')

    turnsTaken = 0

    lastBoard = doubleLastBoard = None

    while not newBoard.gameover():
        doubleLastBoard = lastBoard
        lastBoard = newBoard
        turnsTaken += 1
        newBoard.printBoard()
        if newBoard.playerTurn == 'w':
            print('player move:')
            output = findbestmove(newBoard, 6)
            print('minimax val:', output[1])
            
            newBoard = output[0]
            print('board val:', newBoard.evaluate_board())
        else:
            print('opponents move:')
            output = findbestmove(newBoard, 6)
            print('minimax val:', output[1])
            
            newBoard = output[0]
            print('board val:', newBoard.evaluate_board())

        if doubleLastBoard != None and doubleLastBoard.board == lastBoard.board == newBoard.board:
            print('Tie!')
            break

    newBoard.printBoard()

    if newBoard.bWin():
        print('Black wins!')
    elif newBoard.wWin():
        print('White wins!')
    else:
        print('Draw!')

    print('Turns taken:', turnsTaken)

    



# Function for testing other functions. Makes it easy for me to test things without having to type them in over and over. 
# Leaving it here so that I don't have a file with just one function hanging around awkwardly.
def testinput():

    print(oskaplayer(['----','w--','b-','---','---w'], 'b', 6))
    







    
    
