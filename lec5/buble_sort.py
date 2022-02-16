lis = [13,25,3,24,55,16,79,81,10]

for i in range(len(lis)):
    for j in range(len(lis)-1):
        if lis[j] > lis[j+1]:
            # temp = lis[j+1]
            # lis[j+1] = lis[j]
            # lis[j] = temp
            lis[j], lis[j+1] = lis[j+1], lis[j]
