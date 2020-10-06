import random

class Board:
    def __init__(self,length,width,houses):
        self.length = length 
        self.width = width
        self.houses = houses
        self.board = []
        self.hospital = [] # array that holds the cordinates to each hospital as a touple

    def create2DArray(self):
        self.board = [['0' for i in range(self.length)] for j in range(self.width)]
        # for i in range(self.length): 
        #     col = [] 
        #     for j in range(self.width): 
        #         col.append(' ') 
        #         self.board.append(col) 
                
    def printArray(self):
        # for row in self.board:
        #     print(row) 

        for y in range(self.length):
            for x in range(self.width):
                print( self.board[x][y] ,end = ' ')
            print()

    def insertHospital(self):
        count = 0
        while count < 2:
            tempx = random.randrange(0, self.length)
            tempy = random.randrange(0, self.width)
            if self.board[tempx][tempy] == '0': 
                self.board[tempx][tempy] = 'H'
                self.hospital.append((tempx, tempy))
                count+=1

    
    def insertHouse(self):
        count = 0
        while count < self.houses:
            tempx = random.randrange(0, self.length)
            tempy = random.randrange(0, self.width)
            if self.board[tempx][tempy] == '0':
                self.board[tempx][tempy] = 'h'
                count+=1

    def launch(self):
        self.create2DArray()
        self.insertHospital()
        self.insertHouse()
        self.printArray()


    def __hos_move(self, direction, hosptial_num):
        cord = self.hospital[hosptial_num]
        new_array = self.board
        if direction == "left":
            new_cord = (cord[0]-1, cord[1])
            if new_cord[0] < 0:
                return None
            if self.board[new_cord[0]][new_cord[1]] == '0':
                self.hospital[hosptial_num] = new_cord
                new_array[new_cord[0]][new_cord[1]] = 'H'
                new_array[cord[0]][cord[1]] = '0'
                new_board = Board(self.length, self.width, self.houses)
                new_board.board = new_array
                new_board.hospital = self.hospital
                new_board.hospital[hosptial_num] = new_cord
                new_board.houses = self.houses
                return new_board
        elif direction == "right":
            new_cord = (cord[0]+1, cord[1])
            if new_cord[0] >= self.length:
                return None
            if self.board[new_cord[0]][new_cord[1]] == '0':
                self.hospital[hosptial_num] = new_cord
                new_array[new_cord[0]][new_cord[1]] = 'H'
                new_array[cord[0]][cord[1]] = '0'
                new_board = Board(self.length, self.width, self.houses)
                new_board.board = new_array
                new_board.hospital = self.hospital
                new_board.hospital[hosptial_num] = new_cord
                new_board.houses = self.houses
                return new_board
        elif direction == "up":
            new_cord = (cord[0], cord[1]-1)
            if new_cord[1] < 0:
                return None 
            if self.board[new_cord[0]][new_cord[1]] == '0':
                self.hospital[hosptial_num] = new_cord
                new_array[new_cord[0]][new_cord[1]] = 'H'
                new_array[cord[0]][cord[1]] = '0'
                new_board = Board(self.length, self.width, self.houses)
                new_board.board = new_array
                new_board.hospital = self.hospital
                new_board.hospital[hosptial_num] = new_cord
                new_board.houses = self.houses
                return new_board
        elif direction == "down":
            new_cord = (cord[0], cord[1]+1)
            if new_cord[1] >= self.width:
                return None 
            if self.board[new_cord[0]][new_cord[1]] == '0':
                self.hospital[hosptial_num] = new_cord
                new_array[new_cord[0]][new_cord[1]] = 'H'
                new_array[cord[0]][cord[1]] = '0'
                new_board = Board(self.length, self.width, self.houses)
                new_board.board = new_array
                new_board.hospital = self.hospital
                new_board.hospital[hosptial_num] = new_cord
                new_board.houses = self.houses
                return new_board
        else:
            print("incorrect direction to move the hospital at", cord)

    def move(self):
        """ Method to move the hospitals and return an array of the possible next states. """
        state = []
        direction = ["left", "right", "up", "down"]
        for i in range(2):
            for dir in direction:
                new_state = self.__hos_move(dir, i)
                if new_state is not None:
                    state.append(new_state)
        print(state)
        return state
        

b = Board(3,5,2)

b.launch()
test = b.move()

for i in range(len(test)):
    print(i)
    temp = test[i]
    print(temp.hospital)
    temp.printArray()