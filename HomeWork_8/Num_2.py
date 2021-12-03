s = input()

a = []
for i in range(len(s)):
    if s[i:i+10] in s[i+10:]:
        a.append(s[i:i+10])

print(a)