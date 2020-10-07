from board import Board

print("How many rows?")
rows = int(input())
print("How many cols?")
cols = int(input())
print("How many houses?")
houses = int(input())

b = Board(rows,cols,houses)
b.launch()