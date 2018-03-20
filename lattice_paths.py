
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
