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
