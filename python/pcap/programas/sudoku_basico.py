grid = [[0 for _ in range(9)] for _ in range(9)]

for i in range(9):
  for j in range(9):
    while True:
      try:
        grid[i][j] = int(input(f"Enter value for cell ({i+1},{j+1}): "))
        if 1 <= grid[i][j] <= 9:
          break
        else:
          print("Invalid input. Please enter a number between 1 and 9.")
      except ValueError:
        print("Invalid input. Please enter a number.")

for row in grid:
  print(row)
