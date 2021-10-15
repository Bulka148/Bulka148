#5
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

def getting(first,posi):
    i = 0
    cur = first
    while cur is not None:
        if i == posi:
            return cur.value
        cur = cur.next
        i += 1

first = Pepa(666)
cur = first

for i in range(21):
    cur.next = Pepa(i)
    cur = cur.next

print_list(first)
valka = getting(first, 14)
print(valka)
