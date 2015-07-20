def sieve(num):
    nums = range(2,num)
    for i in range(2,8):
        nums = filter(lambda x: x==i or x%i, nums)
    return nums
