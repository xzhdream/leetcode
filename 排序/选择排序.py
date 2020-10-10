import time

start = time.time()


def sort(l):
    for i in range(len(l) - 1):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j

        if min_index != i:
            l[i], l[min_index] = l[min_index], l[i]
    return l


l = sort([1, 4, 2, 6, 3, 9, 7])
print(l)
print(time.time() - start)
