lis = [13,25,3,24,55,16,79,81,10, 10]

sorted_lis = []

for j in range(len(lis)):
    smallest_so_far = 10000000
    for i in range(len(lis)):
        if lis[i] < smallest_so_far:
            smallest_so_far = lis[i]
            
    sorted_lis.append(smallest_so_far)
    lis.remove(smallest_so_far)   

print(sorted_lis)