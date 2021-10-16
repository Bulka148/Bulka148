a = [1,3,3,4,6,7]
b = [4,4,6,7,8,9,10]
c = []
#RESULT = [1,3,3,4,4,4,6,6,7,7,8,9,10]
ia = 0
ib = 0
if len(b) > len(a):
    a,b = b,a
for ia in range(len(a)):
    while ib < len(b) and b[ib] <= a[ia]:
        c.append(b[ib])
        ib += 1
    c.append(a[ia])

print(c)