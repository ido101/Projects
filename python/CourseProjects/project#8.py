import time
import random


def naive_search(lst, e):
    for i in range(len(lst)):
        if e == lst[i]:
            return i
    return -1


def binary_search(lst, e):
    minimum = 0
    maximum = len(lst) - 1
    while e != lst[(minimum + maximum) // 2]:
        if e > lst[(minimum + maximum) // 2]:
            minimum = (minimum + maximum) // 2 + 1
        if e < lst[(minimum + maximum) // 2]:
            maximum = (minimum + maximum) // 2 - 1
        if minimum > maximum:
            return -1

    return (minimum + maximum) // 2


if __name__ == "__main__":
    # ls = [1, 3, 5, 10, 12]
    # print(binary_search(ls, 10))
    # print(naive_search(ls, 10))

    sorted_list = []
    length = 10000
    while len(sorted_list) < length:
        sorted_list.append(random.randint(-3*length, 3*length))
    sorted_list = sorted(sorted_list)

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print(f"Naive Search Time: {end-start}")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target6)
    end = time.time()
    print(f"Binary Search Time: {end - start}")
