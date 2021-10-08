#2
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

def rev_list(first):
    cur = first
    vals = []
    while cur is not None:
        vals.append(cur.value)
        cur = cur.next
    vals.reverse()

    i = 1
    cur = first
    while cur is not None:
        cur.value = vals[i-1]
        cur = cur.next
        i += 1
    return first

first = Pepa(666)
cur = first

for i in range(21):
    pepa = Pepa(i)
    cur.next = pepa
    cur = cur.next

print_list(first)
first = rev_list(first)
print_list(first)