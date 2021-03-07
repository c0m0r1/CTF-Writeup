with open("subleq64.sq", "r") as f:
    prog = list(map(int,f.read().split()))

prog += [0] * 0x10000

pc = 0 

while pc != -1:
    a, b, c = prog[pc], prog[pc + 1], prog[pc + 2]
    
    # print
    if b == -1:
        print(chr(prog[a] & 0xff))
    prog[b] -= prog[a]

    if prog[b] < -9223372036854775808:
        prog[b] += 0x10000000000000000
    elif prog[b] > 9223372036854775808:
        prog[b] = -0x10000000000000000 + prog[b]

    if prog[b] <= 0:
        pc = c
    else :
        pc += 3
