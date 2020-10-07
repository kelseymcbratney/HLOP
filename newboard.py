import random
import copy
class Board:
    def __init__(self,b_row,b_col,houses):
        self.b_row = b_row # y
        self.b_col = b_col # x
        self.houses = houses # number of total houses on the board
        self.board = None
        self.hospital = [] # array that holds the cordinates to each hospital as a touple
        self.houseCords = [] # array that holds the cordinates to each house as a touple

    def create2DArray(self):
        self.board = [['0' for i in range(self.b_col)] for j in range(self.b_row)] 

    def printArray(self):
        for row in self.board: 
            print(row) 

    def insertHospital(self):
        count = 0
        while count < 2:
            tempx = random.randrange(0, self.b_col)
            tempy = random.randrange(0, self.b_row)
            if self.board[tempy][tempx] == '0': 
                self.board[tempy][tempx] = '@'
                self.hospital.append((tempy, tempx))
                count+=1

    def insertHouse(self):
        count = 0
        while count < self.houses:
            tempx = random.randrange(0, self.b_col)
            tempy = random.randrange(0, self.b_row)
            if self.board[tempy][tempx] == '0':
                self.board[tempy][tempx] = 'H'
                self.houseCords.append((tempy,tempx))
                count+=1

    def launch(self):
        self.create2DArray()
        self.insertHospital()
        self.insertHouse()
        self.printArray()

    def __hos_move(self, direction, hosptial_num):
        cord = copy.copy(self.hospital[hosptial_num])
        new_array = copy.deepcopy(self.board)
        if direction == "left":
            new_cord = (cord[0], cord[1]-1)
            if new_cord[1] < 0:
                return None
            if self.board[new_cord[0]][new_cord[1]] == '0':
                return self.createNewBoard(new_array,new_cord,cord,hosptial_num)
        elif direction == "right":
            new_cord = (cord[0], cord[1]+1)
            if new_cord[1] >= self.b_col:
                return None
            if self.board[new_cord[0]][new_cord[1]] == '0':
                return self.createNewBoard(new_array,new_cord,cord,hosptial_num)
        elif direction == "up":
            new_cord = (cord[0]-1, cord[1])
            if new_cord[0] < 0:
                return None
            if self.board[new_cord[0]][new_cord[1]] == '0':
                return self.createNewBoard(new_array,new_cord,cord,hosptial_num)
        elif direction == "down":
            new_cord = (cord[0]+1, cord[1])
            if new_cord[0] >= self.b_row:
                return None
            if self.board[new_cord[0]][new_cord[1]] == '0':
                return self.createNewBoard(new_array,new_cord,cord,hosptial_num)

    def createNewBoard(self, new_array, new_cord, cord, hosptial_num):
        new_array[new_cord[0]][new_cord[1]] = '@'
        new_array[cord[0]][cord[1]] = '0'
        new_board = Board(self.b_row, self.b_col, self.houses)
        new_board.board = new_array
        new_board.hospital = copy.copy(self.hospital)
        new_board.hospital[hosptial_num] = new_cord
        new_board.houseCords = copy.copy(self.houseCords)
        return new_board

    def move(self):
        state = []
        """ Method to move the hospitals and return an array of the possible next states. """
        state = []
        direction = ["left", "right", "up", "down"]
        for i in range(2):
            for dir in direction:
                new_state = self.__hos_move(dir, i)
                if new_state is not None:
                    state.append(new_state)
        return state

    def calc_distance(self, cord_1, cord_2):
        dist_y = abs(cord_1[0] - cord_2[0])
        dist_x = abs(cord_1[1] - cord_2[1])
        return dist_x + dist_y

    def calc_manhatten(self):
        man_dist = 0
        for house_cord in self.houseCords:
            dist_from_hos_1 = self.calc_distance(self.hospital[0], house_cord)
            dist_from_hos_2 = self.calc_distance(self.hospital[1], house_cord)
            if dist_from_hos_1 <= dist_from_hos_2:
                man_dist += dist_from_hos_1
            else:
                man_dist += dist_from_hos_2
        return man_dist

    def randomize(self):
        for hos in self.hospital:
            self.board[hos[0]][hos[1]] = "0"
        self.hospital = []
        self.insertHospital()
"""
Enjoy my chicken stratch 
"""



def run():
    for i in range(len(test)):
        print(i)
        temp = test[i]
        if temp != None:
            print("New Hospital Cords",temp.hospital)
            print("New Manhatten Distance", temp.calc_manhatten())
            tup1 = (temp,temp.calc_manhatten())
            print(tup1)
            savedStates.append(tup1)
            temp.printArray()


b = Board(7,5,4)
b.launch()

print("*******Original*********")
b.printArray()
b.randomize()
print("*******Random***********")
b.printArray()

print("Orginal Hospital Cords", b.hospital)

test = b.move()
savedStates = []


run()

print(savedStates)

savedStates.sort(key = lambda x:x[1]) # can be used for finding the lowest manhatten distance, index 0 will be new state to move into
lowestManhattan = savedStates[0]

print(savedStates)
print(lowestManhattan[0])

test = lowestManhattan[0]
test = test.move()

run()


