import OskaBoard
import OskaPiece
        


def testinput():

    newBoard = OskaBoard.OskaBoard(['wwww','---','--','---','bbbb'], 'W')
    newBoard.printBoard()

    newBoard2 = OskaBoard.OskaBoard(['wwwww','----','---','--','---','----','bbbbb'], 'W')
    newBoard2.printBoard()

    newBoard3 = OskaBoard.OskaBoard(['wwwww','----','---','---','----','bbbbb'], 'W')

    newBoard4 = OskaBoard.OskaBoard(['wwww-w','---w-','----','---','--','---','-b--','-----','b-bbbb'], 'W')
    newBoard4.printBoard()
