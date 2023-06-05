from random import random
import sys
from typing import List


BOARD_SIZE = 8
NUM_BOMBS = 8
DEFAULT_BLANK_VAL = u"\u2588"
BOMB_VAL = 'X'


class BoardBox(object):
    def __init__(self, value):
        self.value = value
        self.display_value = DEFAULT_BLANK_VAL


class GameBoard(object):
    def __init__(self, board_size: int, num_bombs: int):
        self.setup(board_size, num_bombs)


    def setup(self, board_size: int, num_bombs: int):
        # Create board and return it
        self.size = board_size
        board = [[
            BoardBox(' ') for x in range(board_size)
        ] for y in range(board_size)]

        count = 0
        while count < num_bombs:
            x = int(random() * board_size)
            y = int(random() * board_size)
            if board[x][y].value != BOMB_VAL:
                board[x][y].value = BOMB_VAL
                count += 1

        self.board = self.insert_counts(board)


    def insert_counts(self, board: List[List[BoardBox]]):
        size = len(board)
        for x in range(size):
            for y in range(size):
                if board[x][y].value == BOMB_VAL:
                    continue

                neighbor_count = 0
                neighbor_rows = [-1, 0, 1]
                neighbor_cols = [-1, 0, 1]

                for row_idx in neighbor_rows:
                    target_x = x + row_idx
                    if target_x < 0 or target_x >= size:
                            continue
                    for col_idx in neighbor_cols:
                        target_y = y + col_idx
                        if target_y < 0 or target_y >= size:
                            continue

                        neighbor_count += 1 if board[target_x][target_y].value == BOMB_VAL else 0

                board[x][y].value = str(neighbor_count) if neighbor_count else ' '

        return board


    def parse_input(self, user_input: str):
        if user_input.lower() in ('q', 'quit'):
            sys.exit(0)

        try:
            y, x = (int(num) - 1 for num in user_input.split())
            self.board[x][y].display_value = self.board[x][y].value
            self.clear_blank_neighbors(x, y)
            self.print_board()
        except Exception as e:
            # print('Invalid input')
            print(f'Invalid input: {e}')


    # def clear_blank_neighbors(self, x, y):
    #     if self.board[x][y].value == ' ':
    #         self.board[x][y].display_value = self.board[x][y].value
    #         neighbor_rows = [-1, 0, 1]
    #         neighbor_cols = [-1, 0, 1]

    #         for row_idx in neighbor_rows:
    #             target_x = x + row_idx
    #             if target_x < 0 or target_x >= self.size:
    #                     continue
    #             for col_idx in neighbor_cols:
    #                 target_y = y + col_idx
    #                 if target_y < 0 or target_y >= self.size:
    #                     continue

    #                 if not (x == target_x and y == target_y):
    #                     self.clear_blank_neighbors(target_x, target_y)
    def clear_blank_neighbors(self, x, y, depth=1):
        if self.board[x][y].value != ' ':
            return

        neighbor_rows = [-depth, 0, depth]
        neighbor_cols = [-depth, 0, depth]

        for row_idx in neighbor_rows:
            target_x = x + row_idx
            if target_x < 0 or target_x >= self.size:
                    # continue
                    break
            for col_idx in neighbor_cols:
                target_y = y + col_idx
                if target_y < 0 or target_y >= self.size:
                    # continue
                    break

                if not (x == target_x and y == target_y):
                    if self.board[target_x][target_y].value == ' ':
                        self.board[target_x][target_y].display_value = self.board[target_x][target_y].value
                    self.clear_blank_neighbors(x, y, depth + 1)



    def print_board(self):
        # Iterate through rows and print them
        print('----' * len(self.board[0]) + '-')
        for row in self.board:
            print(f"| {' | '.join([item.display_value for item in row])} |")
            print('----' * len(row) + '-')


def main():
    board_size = sys.argv[1] if len(sys.argv) > 1 else BOARD_SIZE
    num_bombs = sys.argv[2] if len(sys.argv) > 2 else NUM_BOMBS
    board = GameBoard(board_size, num_bombs)

    game_over = False

    while not game_over:
        user_input = input('Enter desired cell: ')

        if board.parse_input(user_input):
            game_over = True

    sys.exit(0)


if __name__ == '__main__':
    main()