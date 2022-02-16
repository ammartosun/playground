def quickSort(L):
    # base case
    if len(L) == 0 or len(L) == 1:
        return L
    
    # pick a pivot "randomly"
    pivot = L.pop(0)

    # split the list in two about the pivot
    left = []
    right = []
    for e in L:
        if e <= pivot:
            left.append(e)
        else:
            right.append(e)
    
    # sort both lists
    left = quickSort(left)
    right = quickSort(right)

    return left + [pivot] + right

L = [99, 5, 5123,12, 4, 69, 45, 1, 8, 0, 1]

print(quickSort(L))

