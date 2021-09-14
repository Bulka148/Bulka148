#Homework
#Задание №4
print(sorted(input())==sorted(input()))

#Задание №5
a = [1,9,9]
x = int(''.join(map(str,a)))
x = x + 1
print()
result = [int(i) for i in str(x)]
print(result)

#Задание №7
s = input()
print(s[::-1])

#Задание №8
a = input()
b = ''.join(i for i in a if i.isalnum())

print(b[::-1] == b)