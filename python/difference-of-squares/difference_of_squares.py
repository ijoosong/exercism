


def difference (num):
    return square_of_sum(num) - sum_of_squares(num)


def sum_of_squares (num):
    """for numbers 1 to num, find the sum of the squares of it"""
    return ( num * ( num + 1 ) * ( 2 * num + 1 ) ) / 6


def square_of_sum (num):
    """for numbers 1 to num, find the sum and square it"""
    return ( num * (num + 1)/2)**2





