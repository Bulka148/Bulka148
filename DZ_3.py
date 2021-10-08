#3
class Pepa:
    def __init__(self, value):
       self.value = value
       self.next = None

def print_list(first):
    cur = first
    while cur is not None:
        print(cur.value, end=" ")
        cur = cur.next
    print(cur)

def sum_2_list(f1, f2):
    sumsum = Pepa(f1.value + f2.value)
    curR = sumsum
    cur1 = f1
    cur2 = f2
    while cur1.next is not None or cur2.next is not None:
        if cur1.next is None:
            cur1.next = Pepa(0)
        elif cur2.next is None:
            cur2.next = Pepa(0)
        cur1 = cur1.next
        cur2 = cur2.next
        curR.next = Pepa(cur1.value + cur2.value)
        curR = curR.next

    return sumsum

f1 = Pepa(666)
f2 = Pepa(333)
cur1 = f1
cur2 = f2

for i in range(21):
    cur1.next = Pepa(i)
    cur2.next = Pepa(i)
    cur1 = cur1.next
    cur2 = cur2.next
for i in range(26,31):
    cur2.next = Pepa(i)
    cur2 = cur2.next

print_list(f1)
print_list(f2)
firR = sum_2_list(f1,f2)
print_list(firR)
