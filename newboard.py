import random
import copy
class Board:
    def __init__(self,b_row,b_col,houses):
        self.b_row = b_row # y
        self.b_col = b_col # x
        self.houses = houses
        self.board = None
        self.hospital = [] # array that holds the cordinates to each hospital as a touple
        self.houseCords = []

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

b = Board(7,5,2)
b.launch()
print("Orginal Hospital Cords", b.hospital)

test = b.move()

for i in range(len(test)):
    print(i)
    temp = test[i]
    if temp != None:
        print("New Hospital Cords",temp.hospital)
        temp.printArray()