s = input()
print(sum([int(s[i])*(-1)**i for i in range(len(s))]))