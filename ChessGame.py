from PIL import Image, ImageTk
import tkinter as tk


class Piece:
    def __init__(self,name, team, type, start):
        self._team = team
        self._type = type
        self._img = team+type+'.png'
        self._start = start
        self._name = name


    def get_img(self):
        return self._img

    #getter
    def get_name(self):
        return self._name
    def get_type(self):
        return self._type
    # getter method
    def get_start(self):
        return self._start
    # getter method
    def get_name(self):
        return self._name
    # getter method
    def get_img(self):
        return self._img
    def get_team(self):
        return self._team


class Tile:
    def __init__(self, name, button):
        self._name = name
        self._button = button
        self._piece = ""

    #setter
    def set_piece(self, piece):
        self._piece = piece

    #getter method
    def get_name(self):
        return self._name
    def get_button(self):
        return self._button
    def get_piece(self):
        return self._piece


class Game:
    def __init__(self):
        self._moveCount = 1;
        self._selectedPiece = ""
        self._confirmedPiece = ""
        self._teamToMove = "w"


    def set_teamToMove(self):
        if self._teamToMove == "w":
            self._teamToMove = "b"
        else:
            self._teamToMove = "w"
        self._selectedPiece = ""
        self._confirmedPiece = ""

    def set_confirmedPiece(self, piece):
        if (piece.get_team() == self._teamToMove):
            self._confirmedPiece = piece
            print(f"selected: {piece}")
        else:
            print("Wrong team selected")

    def get_confirmedPiece(self):
        return self._confirmedPiece
    def get_teamToMove(self):
        return self._teamToMove

    def clear_confirmedPiece(self):
        self._confirmedPiece = ""

    def legalMoveCheck(self, newTile):
        rows = [1, 2, 3, 4, 5, 6, 7, 8]
        piece = self._confirmedPiece
        if piece.get_type() == "p":
            position = pieceLocationDict[piece.get_name()]
            pieceCol = position[0]
            pieceRow = position[1]

            newRow = newTile.get_name()[1]
            newCol = newTile.get_name()[0]

            oldRowIndex = rows.index(int(pieceRow))
            newRowIndex = rows.index(int(newRow))
            oldColIndex = column.index(pieceCol)
            newColIndex = column.index(newCol)

            if position == piece.get_start():
                if (abs(oldRowIndex - newRowIndex) <= 2) and (abs(oldColIndex - newColIndex) == 0):
                    return True
                else:
                    return False
            else:
                if (abs(oldRowIndex - newRowIndex) == 1) and (abs(oldColIndex - newColIndex) == 0):
                    return True
                else:
                    return False

        return True


def createPieces(columns, rows):
    #white pawns
    for i in range(8):
        pieceName = "wp" + str(i + 1)
        pieceDict[pieceName] = Piece("wp" + str(i + 1), "w", "p", columns[i] + "2")
        pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
        tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    #black pawns
    for i in range(8):
        pieceName = "bp" + str(i+1)
        pieceDict[pieceName] = Piece("bp"+str(i+1), "b", "p", columns[i] + "7")
        pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
        tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    #white rooks
    pieceName = "wr1"
    pieceDict[pieceName] = Piece("wr1", "w", "r", "a1")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    pieceName = "wr2"
    pieceDict[pieceName] = Piece("wr2", "w", "r", "h1")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    #black rooks
    pieceName = "br1"
    pieceDict[pieceName] = Piece("br1", "b", "r", "a8")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    pieceName = "br2"
    pieceDict[pieceName] = Piece("br2", "b", "r", "h8")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    #horces
    pieceName = "wh1"
    pieceDict[pieceName] = Piece("wh1", "w", "h", "b1")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    pieceName = "wh2"
    pieceDict[pieceName] = Piece("wh2", "w", "h", "g1")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    pieceName = "bh1"
    pieceDict[pieceName] = Piece("bh1", "b", "h", "b8")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    pieceName = "bh2"
    pieceDict[pieceName] = Piece("bh2", "b", "h", "g8")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    #bishop
    pieceName = "wb1"
    pieceDict[pieceName] = Piece("wb1", "w", "b", "c1")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    pieceName = "wb2"
    pieceDict[pieceName] = Piece("wb2", "w", "b", "f1")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    pieceName = "bb1"
    pieceDict[pieceName] = Piece("bb1", "b", "b", "c8")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    pieceName = "bb2"
    pieceDict[pieceName] = Piece("bb2", "b", "b", "f8")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    #queens
    pieceName = "wq1"
    pieceDict[pieceName] = Piece("wq1", "w", "q", "d1")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    pieceName = "bq2"
    pieceDict[pieceName] = Piece("bq1", "b", "q", "d8")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    #king
    pieceName = "wk1"
    pieceDict[pieceName] = Piece("wk1", "w", "k", "e1")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])
    pieceName = "bk2"
    pieceDict[pieceName] = Piece("bk1", "b", "k", "e8")
    pieceLocationDict[pieceDict[pieceName].get_name()] = pieceDict[pieceName].get_start()
    tileDict[pieceDict[pieceName].get_start()].set_piece(pieceDict[pieceName])

def setupBoard():

    for pieces in pieceDict:
        start = pieceDict[pieces].get_start()
        name = pieceDict[pieces].get_name()
        image = Image.open(pieceDict[pieces].get_img())
        button = buttonDict[start]
        pic = ImageTk.PhotoImage(image)
        buttonDict[start].config(image=pic)
        buttonDict[start].image = pic

def selectPiece(button):

    #if button has piece and there is a selected piece
    if button.get_piece() != "" and game.get_confirmedPiece() != "":
        oldButton = buttonDict[pieceLocationDict[game.get_confirmedPiece().get_name()]]
        movePiece(button.get_button(), oldButton)
        print("ttttttt")
    #if button has piece and there is NO selected piece
    if button.get_piece() != "" and game.get_confirmedPiece() == "":
        game.set_confirmedPiece(button.get_piece())
    #if button has NO piece and there is a selected piece
    if button.get_piece() == "" and game.get_confirmedPiece() != "":
        oldButton = buttonDict[pieceLocationDict[game.get_confirmedPiece().get_name()]]
        movePiece(button.get_button(), oldButton)
    #if button has NO piece and there is NO selected piece
    if button.get_piece() == "" and game.get_confirmedPiece() == "":
        print("No selected piece and no piece on tile")

def movePiece(newButton, oldButton):

    pieceToBeMoved = game.get_confirmedPiece()
    # get tile class ocasiated with buttons
    for key, value in buttonDict.items():
        if value == oldButton:
            oldTile = tileDict[key]

    for key, value in buttonDict.items():
        if value == newButton:
            newTile = tileDict[key]

    if game.legalMoveCheck(newTile):

        image = Image.open(pieceToBeMoved.get_img())
        pic = ImageTk.PhotoImage(image)
        oldButton.config(image="")
        newButton.config(image=pic)
        newButton.image = pic

        # remove piece form old tile, add to new tile
        oldTile.set_piece("")
        newTile.set_piece(pieceToBeMoved)

        # update piece loacation dict
        pieceLocationDict[pieceToBeMoved.get_name()] = newTile.get_name()

        #change team to move and clear confirmed piece
        game.clear_confirmedPiece()
        game.set_teamToMove()


def generateBoard(columns, rows):

    (currentButtonX, currentButtonY) = (0, 0)

    for cNum, c in enumerate(columns, start=1):
        for rNum, r in enumerate(rows, start=1):
            if (cNum+rNum) % 2 == 0:
                color = 'tan'
            else:
                color = 'black'

            buttonName = c + str(r)
            buttonDict[buttonName] = tk.Button(root, height=squareSize, width=squareSize, bg=color)

            # Each tile needs a button
            tileDict[buttonName] = Tile(buttonName, buttonDict[buttonName])

            # Give the buttons colour and a command
            tileDict[buttonName].get_button().config(text=tileDict[buttonName].get_name())
            tileDict[buttonName].get_button().config(command=lambda buttonName = buttonName: selectPiece(tileDict[buttonName]))

            tileDict[buttonName].get_button().place(x=currentButtonX, y=currentButtonY)
            currentButtonY += squareSize
        currentButtonX += squareSize
        currentButtonY = 0


if __name__ == '__main__':

    # Initilise window
    root = tk.Tk()

    # Editing window
    windowSize = 800
    squareSize = int(windowSize/8)
    # Configure window
    root.geometry(f'{windowSize}x{windowSize}+10+10')
    root.title('Chess')

    column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    row = [8, 7, 6, 5, 4, 3, 2, 1]

    #set class dictionarrys
    pieceLocationDict = {}
    buttonDict = {}
    pieceDict = {}
    tileDict = {}

    #game
    game = Game()
    generateBoard(column, row)
    createPieces(column, row)
    setupBoard()

    root.mainloop()




"""
def populateBoard():
    for i in buttonDict:
        if i[1] == '2':
            image = Image.open('wp.png')
            pic = ImageTk.PhotoImage(image)
            buttonDict[i].config(image=pic)
            buttonDict[i].image = pic
        elif i[1] == '7':
            image = Image.open('bp.png')
            pic = ImageTk.PhotoImage(image)
            buttonDict[i].config(image=pic)
            buttonDict[i].image = pic
        elif i[0] in ["a", "h"]:
            if i[1] == "1":
                image = Image.open('wr.png')
                pic = ImageTk.PhotoImage(image)
                buttonDict[i].config(image=pic)
                buttonDict[i].image = pic
            elif i[1] == "8":
                image = Image.open('br.png')
                pic = ImageTk.PhotoImage(image)
                buttonDict[i].config(image=pic)
                buttonDict[i].image = pic
        elif i[0] in ["b", "g"]:
            if i[1] == "1":
                image = Image.open('wh.png')
                pic = ImageTk.PhotoImage(image)
                buttonDict[i].config(image=pic)
                buttonDict[i].image = pic
            elif i[1] == "8":
                image = Image.open('bh.png')
                pic = ImageTk.PhotoImage(image)
                buttonDict[i].config(image=pic)
                buttonDict[i].image = pic
        elif i[0] in ["c", "f"]:
            if i[1] == "1":
                image = Image.open('wb.png')
                pic = ImageTk.PhotoImage(image)
                buttonDict[i].config(image=pic)
                buttonDict[i].image = pic
            elif i[1] == "8":
                image = Image.open('bb.png')
                pic = ImageTk.PhotoImage(image)
                buttonDict[i].config(image=pic)
                buttonDict[i].image = pic
        elif i[0] == "d":
            if i[1] == "1":
                image = Image.open('wq.png')
                pic = ImageTk.PhotoImage(image)
                buttonDict[i].config(image=pic)
                buttonDict[i].image = pic
            elif i[1] == "8":
                image = Image.open('bk.png')
                pic = ImageTk.PhotoImage(image)
                buttonDict[i].config(image=pic)
                buttonDict[i].image = pic
        elif i[0] == "e":
            if i[1] == "1":
                image = Image.open('wk.png')
                pic = ImageTk.PhotoImage(image)
                buttonDict[i].config(image=pic)
                buttonDict[i].image = pic
            elif i[1] == "8":
                image = Image.open('bq.png')
                pic = ImageTk.PhotoImage(image)
                buttonDict[i].config(image=pic)
                buttonDict[i].image = pic

"""

"""
def selectPiece(button):

    if button.get_piece() != "":
        game.selectPiece(button.get_piece())
    else:
        pieceToBeMoved = game.get_confirmedPiece()
        if pieceToBeMoved != "":
            #buttons
            oldButton = buttonDict[pieceLocationDict[pieceToBeMoved.get_name()]]
            newButton = buttonDict[button.get_name()]
            #tiles



            oldButton.config(image="")
            image = Image.open(pieceToBeMoved.get_img())
            pic = ImageTk.PhotoImage(image)
            newButton.config(image=pic)
            newButton.image = pic
            game.set_teamToMove()


            #remove piece form old tile, add to new tile
            oldTile.set_piece("")
            newTile.set_piece(pieceToBeMoved)

            #update piece loacation dict
            pieceLocationDict[pieceToBeMoved.get_name()] = newTile.get_name()
        else:
            print("No piece on tile")

"""





