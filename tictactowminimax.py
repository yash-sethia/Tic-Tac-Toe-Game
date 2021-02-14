class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [
            [ '.', '.', '.' ],
            [ '.', '.', '.' ],
            [ '.', '.', '.' ]
        ]

        self.player_turn = 'X'
        self.result = None


    def draw_board(self):
        for i in range(3):
            for j in range(3):
                print(self.current_state[i][j] + '|', end="")
            print("")
        print("")

    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py> 2:
            return False
        else:
            if self.current_state[px][py] != '.':
                return False
            else:
                return True

    def is_end(self):
        for i in range(3):
            if self.current_state[0][i] != '.' and self.current_state[1][i] != '.' and self.current_state[2][i] != '.' and self.current_state[0][i] == self.current_state[1][i] == self.current_state[2][i]:
                return self.current_state[0][i]

        for i in range(3):
            if self.current_state[i][0] != '.' and self.current_state[i][1] != '.' and self.current_state[i][2] != '.' and self.current_state[i][0] == self.current_state[i][1] == self.current_state[i][2]:
                return self.current_state[i][0]

        if self.current_state[0][0] != '.' and self.current_state[0][0] == self.current_state[1][1] and self.current_state[0][0] == self.current_state[2][2]:
            return self.current_state[0][0]
        if self.current_state[0][2] != '.' and self.current_state[0][2] == self.current_state[1][1] and self.current_state[0][2] == self.current_state[2][0]:
            return self.current_state[0][2]

        for i in range(3):
            for j in range(3):
                if self.current_state[i][j] == '.':
                    return None

        return '.'

    def max(self):
        # Min layer will return the maximum possible value up
        # Return (a, b, c) where a = Heuristic value, (b, c) position where we insert 'O'
        maxv = -2

        px = None
        py = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        else:
            if result == 'O':
                return (1, 0, 0)
            else:
                if result == '.':
                    return (0, 0, 0)


        for i in range(3):
            for j in range(3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'O'
                    (m, min_i, min_j) = self.min()

                    if(m > maxv):
                        maxv = m
                        px = i
                        py = j

                    self.current_state[i][j] = '.'

        return (maxv, px, py)


    def min(self):
        # User plays at this lvel and this level return the minimum value to layer above
        minv = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        else:
            if result == 'O':
                return (1, 0, 0)
            else:
                if result == '.':
                    return (0, 0, 0)

        for i in range(3):
            for j in range(3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()

                    if m < minv:
                        minv = m
                        qx = i
                        qy = j

                    self.current_state[i][j] = '.'


        return (minv, qx,  qy)

    def play(self):
        while True:
            self.draw_board()
            self.result = self.is_end()

            if self.result != None:
                if self.result == 'X':
                    print("The winner is the User i.e. X")
                else:
                    if self.result == 'O':
                        print("The winner is AI i.e. O")
                    else:
                        if self.result == '.':
                            print("It's a draw")

                self.initialize_game()
                return

            if self.player_turn == 'X':
                while True:
                    (m, qx, qy) = self.min()
                    print("You should move at (x, y) = (" + str(qx) + ", " + str(qy) + ")")

                    px = int(input("Enter the X coordinate : "))
                    py = int(input("Enter the Y coordinate :  "))

                    (qx, qy) = (px, py)

                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print("Invalid Move! Try Again")
            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'



g = Game()
g.play()














