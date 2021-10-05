
n = 5
k = 3

a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]


def f(a,b,k):

  for _ in range(k):
    a[a.index(min(a))] = max(b)
    b[b.index(max(b))] = min(a)

  return sum(a)

x = f(a,b,k)

print(x)
