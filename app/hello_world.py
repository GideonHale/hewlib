print('Hello world')

def calc(a, b, op=None):
    """
    Calculator for running operations on two floats

    Parameters:
        a (float, int): first number to be operated on
        b (float, int): second number to be operated on
        op (str): type of operation to be accomplished
    """

    if op == 'add':
        return a + b
    elif op == 'sub':
        return a - b
    elif op == 'mult':
        return a * b
    else:
        return str(a) + str(b)

def fib(n):
    """
    Fancy docstring that clearly describes this function
    """
    # check if the number has already been calculated
    # return if yes
    # conintue if not

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib_dyn(n):

    # this is the array that holds the information we already know
    nums = [0, 1]

    if n == 0 or n == 1:
        return nums[n]
    
    # if we get this far, then n is for sure greater than 1
    for i in range(2, n + 1):
        nums.append(nums[i - 1] + nums[i - 2])
    
    # return the final number in the array
    return nums[n]

def complicated_task(cond):
    if cond == True: # if condition 1 is true
        cond += 1 # then do this or that
        cond = cond + 1 # then do this or that
        exp = cond**42
    # else
        # do this other thing
    # finally return the second to last value of the targets mother-in-law's maiden name
