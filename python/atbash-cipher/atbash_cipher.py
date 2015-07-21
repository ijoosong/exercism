abc = list(map(chr, range(97, 123)))
code = {a:z for (a,z) in zip(abc, reversed(abc))}
code.update({str(x):str(x) for x in range(10)})


def encode(str):
    pre = ''.join(str.split(' ')).lower()
    pre_encoded = ''.join([code[c] for c in pre if c in code])
    return ' '.join([pre_encoded[i:i+5] for i in range(0, len(pre_encoded), 5)])

def decode(str):
    
    return str
