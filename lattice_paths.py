''' PE015 Lattice paths
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner. How many paths exists for 20x20 grid?
'''
a = 20
s = []
for i in range(a):
  s.append(i+2)

for j in range(a-1):
    for i in range(a):
        if i == 0:
            s[i] = s[i] + 1
        else:
            s[i] = s[i] + s[i-1]

print(s[a-1])
