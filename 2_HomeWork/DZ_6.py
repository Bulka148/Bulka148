#№6
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


def list_len(first):
    i = 0
    cur = first
    while cur is not None:
        i += 1
        cur = cur.next
    return i


first = Pepa(999)
cur = first

for i in range(21):
    cur.next = Pepa(i)
    cur = cur.next

print_list(first)
len = list_len(first)
print(len)

