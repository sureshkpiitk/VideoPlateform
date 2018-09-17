import random


class Game:
    def __init__(self, array, key):
        self.array = array
        self.key = key
        self.row, self.column = len(array), len(array[0])

    @staticmethod
    def create_random_number():
        return random.choice([2, 4])

    def collect_empty_place(self):
        empty = []
        for i in range(self.row):
            for j in range(self.column):
                if not self.array[i][j]:
                    empty.append((i, j))
        if not empty:
            raise ValueError("You Lost The Game")
        return random.choice(empty)

    def set_value_random(self):
        random_number = Game.create_random_number()
        empty_places = self.collect_empty_place()
        self.array[empty_places[0]][empty_places[1]] = random_number

    def shift_left(self):
        if self.key == 1:
            for i in range(self.row):
                temp_j = -1
                for j in range(self.column):
                    if self.array[i][j]:
                        if temp_j >= 0 and self.array[i][temp_j] == self.array[i][j]:
                            self.array[i][temp_j] += self.array[i][j]
                            self.array[i][j] = 0
                        elif temp_j >= 0 and not self.array[i][temp_j]:
                            self.array[i][temp_j], self.array[i][j] = self.array[i][j], self.array[i][temp_j]
                            continue
                        else:
                            self.array[i][temp_j+1], self.array[i][j] = self.array[i][j], self.array[i][temp_j+1]
                        temp_j += 1

        else:
            raise ValueError("Unexpected Key Enter")

    def shift_right(self):
        if self.key == 3:
            for i in range(self.row):
                temp_j = self.column
                for j in range(self.column-1, -1, -1):
                    if self.array[i][j]:
                        if temp_j <= self.column - 1 and self.array[i][temp_j] == self.array[i][j]:
                            self.array[i][temp_j] += self.array[i][j]
                            self.array[i][j] = 0
                        elif temp_j <= self.column - 1 and not self.array[i][temp_j]:
                            self.array[i][temp_j], self.array[i][j] = self.array[i][j], self.array[i][temp_j]
                            continue
                        else:
                            self.array[i][temp_j - 1], self.array[i][j] = self.array[i][j], self.array[i][temp_j - 1]
                        temp_j -= 1
        else:
            raise ValueError("Unexpected Key Enter")

    def shift_up(self):
        if self.key == 2:
            for i in range(self.column):
                temp_i = -1
                for j in range(self.row):
                    if self.array[j][i]:
                        if temp_i >= 0 and self.array[temp_i][i] == self.array[j][i]:
                            self.array[temp_i][i] += self.array[j][i]
                            self.array[j][i] = 0
                        elif temp_i >= 0 and not self.array[temp_i][i]:
                            self.array[temp_i][i], self.array[j][i] = self.array[j][i], self.array[temp_i][i]
                            continue
                        else:
                            self.array[temp_i + 1][i], self.array[j][i] = self.array[j][i], self.array[temp_i + 1][i]
                        temp_i += 1
        else:
            raise ValueError("Unexpected Key Enter")

    def shift_down(self):
        if self.key == 4:
            for i in range(self.column):
                temp_i = self.row
                for j in range(self.row-1, -1, -1):
                    if self.array[j][i]:
                        if temp_i <= self.row - 1 and self.array[temp_i][i] == self.array[j][i]:
                            self.array[temp_i][i] += self.array[j][i]
                            self.array[j][i] = 0
                        elif temp_i <= self.row - 1 and not self.array[temp_i][i]:
                            self.array[temp_i][i], self.array[j][i] = self.array[j][i], self.array[temp_i][i]
                            continue
                        else:
                            self.array[temp_i - 1][i], self.array[j][i] = self.array[j][i], self.array[temp_i - 1][i]
                        temp_i -= 1
        else:
            raise ValueError("Unexpected Key Enter")

    def __call__(self, *args, **kwargs):
        if self.key == 1:
            self.shift_left()
        elif self.key == 2:
            self.shift_up()
        elif self.key == 3:
            self.shift_right()
        elif self.key == 4:
            self.shift_down()
        self.set_value_random()


n, m = 4, 6  # Size of game As n- Row m- Column
loop = True
array = [[0 for x in range(m)] for y in range(n)]
while loop:
    input_ = eval(input("Enter Number 1 For Left, 2 for Up, 3 for Right and 4 for Down And 0 For Exit"))
    Game(array, input_).__call__()
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end='          ')
        print()
    if input_ == 0:
        loop = False

