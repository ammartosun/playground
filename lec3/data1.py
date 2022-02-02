from copy import deepcopy


lis = [2,3,4]

# for i in range(0,len(lis)):
#     print(lis[i])

# for e in lis:
#     print(e)


def add(lis):
    sum = 0
    for e in lis:
        sum += e
    return sum

sum = add(lis)
print(sum)

def squareList(a):
    sqrlis = []
    for e in a:
        sqrlis.append(e*e)

    return sqrlis


sqrlis = squareList([1,2,3,4])
print(sqrlis)

lis = [123, 1, 2, 'q', 'q', 3, 'q']
# while 'q' in lis:
#     lis.remove('q')
#     lis.pop(5)

# print(lis[3])

# lis.reverse()
# print(lis)


def copyList(a):
    copy = []
    for e in a:
        copy.append(e)
    return copy

x = [1,2,3]
#y = copyList(x)

y = deepcopy(x)

print(x == y)
print(x is y)