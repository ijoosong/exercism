def distance(orig, new):
    count = 0
    for x in range(0, len(orig)):
        if not orig[x] == new[x]:
            count+=1
    return count
