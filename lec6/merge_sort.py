def merge(L1, L2):
    result = []

    while len(L1) != 0 and len(L2) != 0:
        if L1[0] <= L2[0]:
            result.append(L1.pop(0))
        else:
            result.append(L2.pop(0))
    
    if len(L1) > 0:
        result = result + L1
    else:
        result = result + L2

    return result

def mergeSort(L):
    # base case
    if len(L) == 0 or len(L) == 1:
        return L
    
    # split the list in two  [1,2,3,4,5]
    mid = len(L) // 2
    left = L[:mid]          #[1,2]
    right = L[mid:]         #[3,4,5]

    #sort both sublists
    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


L = [99, 5, 5123,12, 4, 69, 45, 1, 8, 0, 1]
print(mergeSort(L))