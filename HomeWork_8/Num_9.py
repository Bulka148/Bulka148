a = list(map(int, input().split()))
b = list(map(int, input().split()))

if len(a) < len(b):
    a, b = b, a

b += [1]*(len(a)-len(b))

for i in range(len(a)):
    a[i] *= b[i]

print(a)