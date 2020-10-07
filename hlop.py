from board import Board

print("How many rows?")
rows = int(input())
print("How many cols?")
cols = int(input())
print("How many houses?")
houses = int(input())
print("Hillclimb or Simulated Annealing? (1, or 2)")
algo = input()

b = Board(rows,cols,houses)
b.launch()