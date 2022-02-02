'''
@input a: value 1
@input b: value 2
@return: sum of value 1 and 2
''' 
a = 1001

def add(x, y):
    sum2 = add2(x, y)
    main(a, 100)
    return sum2

def main(x, y):
    global a
    print(a)
    return a

def add2(x, y):
    sum = add(1, 3) # 1007

    sum2= add2(a, 1002) # 1010

    if sum > sum2:
        print(sum2)
    
    print(sum)


main(a, 55)

# 1004
# 1007
# 1007