__author__ = 'phizaz'

# the game is playing alternatively from player1, player2 and player1 and so on...
class TicTacToe:
    def __init__(self):
        self.ended = None
        self.player = None
        # init table
        self.table = None
        self.restart()

    def restart(self, start=1):
        # start with player 1
        self.ended = False
        self.player = start
        self.table = [[0 for i in range(3)] for i in range(3)]
        # restart always success
        return self.table

    def turn(self, action):
        y, x = action
        valid = self.is_action_valid(action)
        if not valid:
            # no action taken
            return None
        # take action and move
        # player 1 is 1
        # player 2 is 2
        self.table[y][x] = self.player
        self.player = 2 if self.player is 1 else 1
        # return winning result
        return self.is_end()

    def is_action_valid(self, action):
        # check if the action is valid
        # here....
        y, x = action
        valid = self.table[y][x] == 0 \
                and not self.is_end()
        return valid

    def display(self):
        # print in tabular form
        print('')
        for i in range(3):
            print('-', end='')
        print('')
        for i in range(3):
            for j in range(3):
                print(self.table[i][j], end='')
            print('')
        for i in range(3):
            print('-', end='')
        print('')

    def is_end(self):
        if self.ended is False:
            winner = self.winner()
            self.ended = winner if winner is not None else False
        return self.ended

    def winner(self):
        # no winner at first
        winner = None

        def is_identical(alist):
            return len(set(alist)) == 1

        def is_winning(alist):
            nonlocal winner
            if alist[0] is not 0 and is_identical(alist):
                winner = alist[0]
                return True
            else:
                return False

        for row in range(3):
            horizontal = [self.table[row][i] for i in range(3)]
            if is_winning(horizontal):
                break
        for col in range(3):
            vertical = [self.table[i][col] for i in range(3)]
            if is_winning(vertical):
                break

        diagonal_left = [self.table[i][i] for i in range(3)]
        is_winning(diagonal_left)

        diagonal_right = [self.table[i][3-i-1] for i in range(3)]
        is_winning(diagonal_right)

        return winner
