def sum_of_multiples(num, *args, **kwargs):
    factors = [3, 5]
    buff = []
    if args:
        print args[0]
        factors = [x for x in args[0]]
    nums = range(num)
    for num in factors:
        buff.append((filter(lambda x:x%num==0, nums))

    return total
