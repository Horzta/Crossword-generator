import string
import random


class Crossword:
    def __init__(self, word_list):
        self.word_list = word_list

    def max_length(self):
        max_size = 0
        for word in self.word_list:
            if len(word) > max_size:
                max_size = len(word)
        return int(max_size*2)

    def print(self):
        board = []
        for y in range(self.max_length()):
            x_array = []
            for x in range(crossword.max_length()):
                letter = Boardtile(random.choice(string.ascii_uppercase))
                x_array.append(letter)
            board.append(x_array)

        for word in self.word_list:
            point_x = 0
            point_y = 0
            direction = ''
            possible = False

            while not possible:
                point_x = random.choice(range(self.max_length()))
                point_y = random.choice(range(self.max_length()))
                direction = random.choice(['horizontal', 'vertical'])

                print("Trying for coordinates", point_y, point_x, " at direction ",direction)

                if (direction is 'horizontal' and point_x + len(word) > self.max_length()) \
                        or (direction is 'vertical' and point_y + len(word) > self.max_length()):
                    continue

                for index in range(0, len(word)):
                    if direction is 'horizontal':
                        temp_point_x = point_x + index
                        temp_point_y = point_y
                    else:
                        temp_point_y = point_y + index
                        temp_point_x = point_x

                    if not board[temp_point_y][temp_point_x].isUpdatable():
                        print(["Coordinates ", temp_point_y, temp_point_x, " is not updatable."])
                        break

                    possible = True

            for index in range(0, len(word)):
                letter = word[index]
                if direction is 'horizontal':
                    temp_point_x = point_x + index
                    temp_point_y = point_y
                else:
                    temp_point_y = point_y + index
                    temp_point_x = point_x

                board[temp_point_y][temp_point_x].update(letter)

            print("Now trying to print " + word)
            print(["Going " + direction + " at point ", point_y, point_x])

        for y in range(self.max_length()):
            print(*board[y], sep="")

class Boardtile:
    def __init__(self,letter):
        self.letter = letter
        self.updatable = True

    def __str__(self):
        return self.letter

    def getLetter(self):
        return self.letter

    def update(self, letter):
        self.letter = letter
        self.updatable = False

    def isUpdatable(self):
        return self.updatable

word_list = ['ORANGE', 'APPLE', 'PEAR', 'STRAWBERRY', 'BANANA']
crossword = Crossword(word_list)
print(["Max size is: ", crossword.max_length()])
crossword.print()

