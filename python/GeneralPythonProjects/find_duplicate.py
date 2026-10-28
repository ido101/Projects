import random


def find(l):
    new_lst = sorted(l)
    d = new_lst[0]
    for i in new_lst[1:]:
        if d == i:
            return d
        d = i


n = random.randint(1, 10)
lst = [random.randint(1, n) for _ in range((n + 1))]
print(f"list: {lst}\nduplicate:{find(lst)}")
