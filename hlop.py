#Artificial Intelligence A405
from board import Board
from copy import deepcopy
from solver import Solver

print("How many rows?")
rows = int(input())
print("How many cols?")
cols = int(input())
print("How many houses?")
houses = int(input())
print("Hillclimb or Simulated Annealing? (1, or 2) or Press 3 to run them all four times")
algo = int(input())


if algo == 1 or algo == 2:
    b = Board(rows,cols,houses)
    print("ORIGINAL BOARD")
    b.launch()
    print("OLD MANHATTEN", b.calc_manhatten())
    s = Solver(b,algo)
    print("NEW MANHATTEN", s.beststate.calc_manhatten())
    s.beststate.printArray()

elif algo == 3:
    b1 = Board(rows,cols,houses)
    #print("ORIGINAL BOARD")
    b1.launch()
    #print("Manhatten Distance:", b1.calc_manhatten())

    for i in range(4):
        print("*********Start Board*****************")
        print("Original Manhatten Distance:", b1.calc_manhatten())
        #b1.printArray()

        s1_1_hillclimb = Solver(deepcopy(b1), 1)
        print("**********Hillclimb solution w/ Random Restart**********")
        print("New Random Restart Manhatten Distance:", s1_1_hillclimb.beststate.calc_manhatten())
        #s1_1_hillclimb.beststate.printArray()

        s1_1_annealing = Solver(deepcopy(b1), 2)
        print("*****Simulated Annealing solution****")
        print("New Simulated Annealing Manhatten Distance:", s1_1_annealing.beststate.calc_manhatten())
        #s1_1_annealing.beststate.printArray()
        b1.randomize()

