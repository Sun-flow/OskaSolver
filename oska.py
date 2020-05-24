import OskaBoard

# Required move-generation function.
# 
# Inputs: Oska board of any length as list, moving player's turn
# 
# Return: List of boards that can be reached from current board in a single move  
def movegen(inBoard, playerTurn):
    Board = OskaBoard.OskaBoard(inBoard, playerTurn)
    return Board.generatechildren()


def movepiece(inBoard):
    print('Decide which piece you want to move.')
    startRow = int(input('Starting row:'))
    startCol = int(input('Starting col:'))
    direction = input('Dir:')

    newBoard = inBoard.movepiece(startRow, startCol, direction)
    return newBoard[0]


def minimax(board, depth, maxing):
    if depth == 0 or board.gameover():
        return (board, board.boardeval())
    
    bestBoard = None

    if maxing:
        maxVal = -999999999999
        for child in board.generatechildren():
            curVal = minimax(child, depth - 1, False)
            if curVal[1] > maxVal:
                maxVal = curVal[1]
                bestBoard = child
        return (bestBoard, maxVal)

    else:
        minVal = 9999999999999
        for child in board.generatechildren():
            curVal = minimax(child, depth - 1, True)
            if curVal[1] < minVal:
                minVal = curVal[1]
                bestBoard = child
        return (bestBoard, minVal)


def findbestmove(board):
    if board.playerTurn == 'w':
        return minimax(board, 5, True)
    else:
        return minimax(board, 5, False)


def playgame():
    color = input('Would you like to be black or white? b/w')

    newBoard = OskaBoard.OskaBoard(['wwwww','----','---','--','---','----','bbbbb'], 'w')

    while not newBoard.gameover():
        newBoard.printBoard()
        if newBoard.playerTurn == color:
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

    newBoard.printBoard()

    if newBoard.bWin():
        print('Black wins!')
    elif newBoard.wWin():
        print('White wins!')

    



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
    
