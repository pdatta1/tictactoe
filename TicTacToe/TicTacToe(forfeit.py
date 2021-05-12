from linkedlist import LinkedList


def main():
    # Change for number for rows, second for columns, third for numbers to get in a row to win.
    TicTacToe(3, 3, 3)

class TicTacToe:

    def __init__(self, row=3, col=3, winNum=3):
        self.board = LinkedList()
        self.row = row
        self.col = col
        self.size = row * col
        self.winNum = winNum
        self.createBoard(row, col)
        self.play()

    def createBoard(self, row, col):
        for i in range(col):
            self.board.insert(i, [])
            for k in range(row):
                self.board[i].append(0)
        # print(self.board)
        # self.drawBoard()

    def drawBoard(self):
        total = 0
        player = 0
        for i in range(self.row):
            d = self.board
            for k in range(self.col):
                if d[i][k] == .1:
                    player = "X"
                elif d[i][k] == .2:
                    player = "O"
                else:
                    player = total
                if k < self.col - 1:
                    print("%s | " % (player), end="")
                else:
                    print("%s " % (player), end="")
                total += 1
            print("\n", end="")
            if i < self.row - 1:
                print("----------", end="")
            print("\n", end="")

    def playerMove(self, player):
        turn = True
        while turn:
            total = 0
            xo = "X"
            if player == .2:
                xo = "O"
            pos = int(input(f"Player {player * 10:.0f} ({xo}), Pick position: "))
            for i in self.board:
                count = 0
                for k in i[:]:
                    try:
                        if pos == 100:
                            self.drawBoard()
                            count =0
                            total = 0
                            turn = False
                            TicTacToe(3, 3, 3)

                            return
                        if total == pos and i[count] != .1 and i[count] != .2:
                            i[count] = player
                            self.drawBoard()
                            turn = False
                            return
                    except:
                        if total == pos and i[count] != .1 and i[count] != .2:
                            i[count] = player
                            self.drawBoard()
                            turn = False
                            return
                    total += 1
                    count += 1

    def consecCount(self, toCheck):
        count = 0
        for i in range(self.row - 1):
            # getting Consecutive elements
            try:
                if toCheck[i] == toCheck[i + 1]:
                    count += 1
                    if count == self.winNum - 1:
                        return toCheck[i]
                else:
                    count = 0
            except:
                continue
        return None

    def winner(self, winCondition):
        if self.consecCount(winCondition) == .1:
            print("Player 1 Wins!")
            return True
        elif self.consecCount(winCondition) == .2:
            print("Player 2 Wins!")
            return True
        else:
            return False

    def checkWin(self):
        winCondition = []
        b = self.board
        # Checks the Row win condition
        for i in self.board:
            for k in i[:]:
                winCondition.append(k)
            if self.winner(winCondition):
                return True
            winCondition.clear()
        # Checks Column win condition
        for k in range(self.col):
            for i in self.board:
                winCondition.append(i[k])
                if self.winner(winCondition):
                    return True
            winCondition.clear()
        # Checks for Diagonal down win condition
        for i in range(self.row):
            winCondition.append(self.board[i][i])
        if self.winner(winCondition):
            return True
        winCondition.clear()
        # Checks for Diagonal up win condition
        for i in range(self.row-1, -1, -1):
            winCondition.append(self.board[self.row-1-i][i])
        if self.winner(winCondition):
            return True
        winCondition.clear()
        return False

    def play(self):
        self.drawBoard()
        print("forfeit match and restart by typing in 100")
        win = False
        count = 0
        while not win:
            # Player 1 = .1 and Player 2 = .2
            # This is to make it easier to draw positions 1 and 2 without having an X or O on  them
            player = .1
            self.playerMove(player)
            count += 1
            if self.checkWin():
                again = int(input("Press 1 to play again or 0 to end: "))
                if again >= 1:
                    TicTacToe(3, 3, 3)
                    count = 0
                else:
                    win = True
                break





            if count >= 9:
                print("Tie Game!")
                again = int(input("Press 1 to play again or 0 to end: "))
                if again >= 1:
                    TicTacToe(3, 3, 3)
                    count = 0
                else:
                    win = True
                break

            player += .1
            self.playerMove(player)
            count += 1
            if self.checkWin():
                again = int(input("Press 1 to play again or 0 to end: "))
                if again >= 1:
                    TicTacToe(3, 3, 3)
                    count = 0
                else:
                    win = True
                break
            print(count)




main()
