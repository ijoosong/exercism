def sum_of_multiples(num, *args, **kwargs):
    factors = [3, 5]
    buff = []
    if args:
        print args[0]
        factors = [x for x in args[0] if x > 0]
    nums = range(1,num)

    for i in range(len(factors)):
        if i == 0:
            buff.append(filter(lambda x:x%factors[i]==0, nums))
        else:
            buff.append( filter(lambda x:x%factors[i]==0 and x not in buff[i-1], nums))
    total = 0
    for li in buff:
        total += sum(li)
        print li
    return total
