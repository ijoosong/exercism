def sieve(num):
    nums = range(2,num+1)

    for i in range(2,num+1):
        nums = filter(lambda x: x==i or x%i, nums)
    return nums
