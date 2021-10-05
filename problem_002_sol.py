


n = int(input())
x = []

def setting(data):
  return data[1]
  
for i in range(n):
  a, b = input().split(' ')
  
  x.append((a, int(b)))

print(x)


y = sorted(x, key = setting)

for i in range(len(y)):

  print(y[i][0])
