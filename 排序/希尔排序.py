#核心思想：通过间隙进行分组，然后组内插入,执行多次

import math


def sort(l):
    gap = 1
    while gap < len(l):
        gap = gap*3+1

    while gap > 0:
        for i in range(gap,len(l)):
            temp = l[i]
            j = i - gap
            while l[j] > temp:
               l[j+gap] = l[j]
               j -= gap
            l[j+gap] = temp
        gap = math.floor(gap/3)

    return l


l = [1,3,6,2,4,7,8,3]
print(sort(l))

