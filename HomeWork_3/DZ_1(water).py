a = [1, 5, 4, 2, 4, 1]
l = len(a)
m = 0
cur = 0

for i in range(l):
    for j in range(i+1, l):
        cur = (j - i) * min(a[i], a[j]) + 0.5 * ((j - i) * (max(a[i], a[j]) - min(a[i], a[j])))
        if cur > m:
            m = cur
print(m)