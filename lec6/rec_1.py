def dec_for(n):
    for _ in range(n):
        print("*")

def dec_rec(n):
    # base case
    if n == 1:
        print("*")
    
    # recursive case
    else:
        print("*")  # step
        dec_rec(n-1)
    

# dec_for(5)
# dec_rec(5)

# n! = n*n-1*n-2*...*3*2*1
# 1! = 1
# 0! = 1
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

# print(fac(5))


def fib(n):
    '''fib(n) = fib(n-1) + fib(n-2) '''
    # fib 4 = fib 3 + fib 2 = 2 + 1 = 3
    # fib 3 = fib 2 + fib 1 = 1 + 1 = 2
    # fib 2 = fib 1 + fib 0  = 1 + 0 = 1

    # fib 1 = 1
    # fib 0 = 0

    # base
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)


# print(fib(40))

'''returns the sum of all integers in the list L'''
def sum_list(L):
    # base case
    if len(L) == 0:
        return 0
    
    return L[0] + sum_list(L[1:])

L = [1,2,3,4,5]
sum_list(L)
