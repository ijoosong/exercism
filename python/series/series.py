def slices(num, it):
    x = map(lambda i:int(i), num)
    temp = it
    li = []
    if it > len(x):
        raise ValueError('The iteration number it: %i is longer than length of num: %i' % (it, len(x)))
    elif it == 0:
        raise ValueError('it is 0 and thus wont work')
    else:
        for i in range (len(x)-it+1):
            li.append(x[i:temp])
            temp += 1
    return li
