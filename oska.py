import OskaBoard

# Required move-generation function.
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



# Finds the best possible move for a given player (according to boardeval).
# 
# Inputs: an OskaBoard, searchdepth, whether or not the function is maxing or not (boolean)
# 
# Return: tuple: (new board, board's minimax val) 
def minimax(board, depth, alpha, beta, maxing):
    if depth == 0 or board.gameover():
        return (board, board.boardeval())
    
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



# Runs minimax algorithm for player whose turn it is.
# 
# Inputs: an OskaBoard
# 
# Return: tuple: (new board, board's minimax val) 
def findbestmove(board):
    if board.playerTurn == 'w':
        return minimax(board, 6, -9999999999999, 9999999999999, True)
    else:
        return minimax(board, 6, -9999999999999, 9999999999999, False)



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
            print('board val:', newBoard.boardeval())
        else:
            print('opponents move:')
            output = findbestmove(newBoard)
            print('minimax val:', output[1])
            
            newBoard = output[0]
            print('board val:', newBoard.boardeval())

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
            output = findbestmove(newBoard)
            print('minimax val:', output[1])
            
            newBoard = output[0]
            print('board val:', newBoard.boardeval())
        else:
            print('opponents move:')
            output = findbestmove(newBoard)
            print('minimax val:', output[1])
            
            newBoard = output[0]
            print('board val:', newBoard.boardeval())

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

    newBoard = OskaBoard.OskaBoard(['wwww','---','--','---','bbbb'], 'b')
    newBoard.printBoard()


    #print(newBoard.moveprep((0,1),newBoard.wPieces.index((0,1)), False))
    #print(newBoard.moveprep((2,1),newBoard.bPieces.index((2,1)), False))

    print(newBoard.boardeval())
    #newBoard = movepiece(newBoard)
    #newBoard.printBoard()
    #newBoard = movepiece(newBoard)
    #newBoard.printBoard()
    #bestMove = findbestmove(newBoard)
    #print('minimax value:',bestMove[1])
    #bestMove[0].printBoard()



    #eval = newBoard.boardeval()
    #print('eval: ', eval)


    #newBoard2 = OskaBoard.OskaBoard(['b----','----','---','-w','--w','----','-----'], 'W')
    #newBoard2.printBoard()

    #eval = newBoard2.boardeval()
    #print('eval: ', eval)

    #newBoard3 = OskaBoard.OskaBoard(['wwwww','----','---','---','----','bbbbb'], 'W')

    #newBoard4 = OskaBoard.OskaBoard(['wwww-w','---w-','----','---','--','---','-b--','-----','b-bbbb'], 'W')
    #newBoard4.printBoard()

    #newBoard5 = OskaBoard.OskaBoard(['wwww','w--','--','---','bbbb'], 'W')
    #newBoard5.printBoard()

    #newBoard6 = OskaBoard.OskaBoard(['wwwq','---','--','---','bbbb'], 'W')
    #newBoard6.printBoard()

    
    #newChildren = newBoard.generatechildren()
    #for child in newChildren:
    #    child.printBoard()

    #newChildren2 = generatechildren(newBoard2, 'w')
    #for child in newChildren2:
    #    child.printBoard()

    #newChildren7b = movegen(newBoard7, 'b')
    #for child in newChildren7b:
    #    child.printBoard()

    #newChildren7w = movegen(['--ww--','--b--','-w--','-b-','-w','---','----','-----','------'], 'b')
    #for child in newChildren7w:
    #    child.printBoard()
    
