
n = input()
x = []

for i in range(int(n)):
  x.append(int(input()))

x.sort(reverse=True)

print(x)
