import os


"""
We'll obviously want 2 players: p1 and p2
I think there's probably an argument to create a computer player, but if that's
not requested, don't take on that burden

The board will most likely be a 2D list

How do we prompt users to select a position on the board?

If we're using a UI, that makes things simultaneously easier and more difficult


"""

class TicTacToeBoard(object):
    def __init__(self):
        # self.board = [[None] * 3] * 3
        self.board = [[None, None, None], [None, None, None], [None, None, None]]

    def printBoard(self):
        print(
            "\n\n".join(
                "  ".join(item.char if item else " " for item in row)
                    for row in self.board
            )
        )

    def insert(self, player, idx):
        d = {
            'A': 0,
            'B': 1,
            'C': 2,
        }
        idx = idx.upper()
        row, col = idx
        self.board[d[row]][int(col)] = player

    def hasEmptySpaces(self):
        for row in self.board:
            if None in row:
                return True
        return False

    def checkForWinner(self):
        # Check for matching row
        for row in self.board:
            s = set(row)
            if len(s) == 1 and None not in s:
                print('yay1')
                return s.pop()
        
        # Check for matching column
        for i in range(len(self.board[0])):
            s = set(row[i] for row in self.board)
            if len(s) == 1 and None not in s:
                print('yay2')
                return s.pop()
            
        # Check for diagonal match
        d1s = set()
        d2s = set()
        for i in range(len(self.board)):
            d1s.add(self.board[i][i])
            d2s.add(self.board[i][len(self.board) - 1 - i])
        if len(d1s) == 1 and None not in d1s:
            print('yay3')
            return d1s.pop()
        if len(d2s) == 1 and None not in d2s:
            print('yay4')
            return d2s.pop()
        return None


class Player(object):
    def __init__(self, playerID, char):
        self.playerID = playerID
        self.char = char


def validateIdxSelection(idx):
    if not idx:
        return False
    row, col = idx
    print(row, col)
    if row.upper() not in 'ABC' or col not in '012':
        print('bad')
        return False
    return True


def main():
    board = TicTacToeBoard()
    winner = None
    p1 = Player(1, 'X')
    p2 = Player(2, 'O')
    curPlayer = p1
    while board.hasEmptySpaces() and not winner:
        idx = None
        while not validateIdxSelection(idx):
            idx = input(f"Player {curPlayer.playerID} select board idx: ")
        board.insert(curPlayer, idx)
        winner = board.checkForWinner()
        curPlayer = p1 if curPlayer == p2 else p2
        board.printBoard()
    if winner:
        print(f"Player {winner.playerID} wins!")
    else:
        print("Tie!")


if __name__ == "__main__":
    main()