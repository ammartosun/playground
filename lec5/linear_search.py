lis = [13,25,3,24,55,16,79,81,10]



# find x
x = 10

for i in range(len(lis)):
    if lis[i] == x:
        print("Found " + str(x) + " at " + str(i) + "th step.")
        break
    else:
        continue