import time

start = time.time()

# x:0.6276040077209473
# y:0.9831290245056152
def sort1(l):
    for i in range(1, len(l)):
        for j in range(len(l) - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


# x:0.0009810924530029297
# y:0.9825119972229004
def sort2(l):
    tag = 1
    for i in range(1, len(l)):
        if tag == 1 and i > 1:
            print(i)
            return l
        else:
            tag = 1
        for j in range(len(l) - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                tag = 0
    return l


x = [1] * 1000 + [2] * 1000 + [5] * 1000
y = [1, 2, 5] * 1000

l = sort1(y)
print(l)
print(time.time() - start)


# 在已排好序的情况下，方法2时间更短
# 乱序情况下，方法2时间更短
# 完全乱序情况下，二者时间相同
