#
# Skeleton file for the Python "Bob" exercise.
#
def hey(what):
#if question respond sure (? at the end minus white space)
#if all caps and no question respond Whoa, chill out!
#if any whitespace or punctuation Fine. Be that way!
#anything else - whatever

    response_q = "Sure."
    response_y = "Whoa, chill out!"
    response_a = "Fine. Be that way!"
    response_w = "Whatever."
    if what.isupper():
        return response_y
    elif what.rstrip().endswith('?'):
        return response_q
    elif not what.strip():
        return response_a
    else:
        return response_w

