rows = 5
for i in range(1, rows + 1):
  # Outer loop controls the number of rows
  for s in range(5 - i):
    print(end=" ")
  for j in range(1, 2 * i):
    # Inner loop prints asterisks for each row
    print("*", end="")
  print()  # Move to a new line after each row of asterisks