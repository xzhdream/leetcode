#核心思想：循环取出列表中的数，然后将数字向前比较，插入合适位置

import time

start = time.time()


def sort(l):
    for i in range(len(l)):
        index = i - 1
        current = l[i]
        while index >= 0 and l[index] > current:
            l[index + 1] = l[index]
            index -= 1
        l[index + 1] = current
    return l


l = sort([1, 3, 2, 5, 6, 4, 9, 0, 7, 6])
print(l)
print(time.time()-start)
