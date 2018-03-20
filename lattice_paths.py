''' PE015 Lattice paths
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner. How many paths exists for 20x20 grid?
'''
grid = 20
route = []

for i in range(grid):
  route.append(i+2)

for j in range(grid-1):
    for i in range(grid):
        if i == 0:
            route[i] = route[i] + 1
        else:
            route[i] = route[i] + route[i-1]

print(route[grid-1])
