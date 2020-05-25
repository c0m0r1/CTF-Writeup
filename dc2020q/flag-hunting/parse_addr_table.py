from pwn import *

def parse_line(l):
    return (line.split()[0], line.split()[1], " ".join(line.split()[2:]))

with open("trace_libc.txt","r") as f:
    trace = f.read().strip()

prev_sym = None
sym_dict = {}

for line in trace.split("\n"):
    if prev_sym == None:
        prev_sym = parse_line(line)
        continue

    sym = parse_line(line)

    if prev_sym[1] == "jmp" or prev_sym[1] == "call":
        try: #direct
            sym_dict[sym[0]] = int(prev_sym[2], 16)
        except ValueError as e: #indirect
            if "rip" in prev_sym[2]: #rip-relative call
                offset = int(prev_sym[2].split("+")[1][:-1], 16)
                # todo

    prev_sym = sym

f = open("trace_addr_transed.txt","w")
for line in trace.split("\n"):
    sym = parse_line(line)
    if sym[0] in sym_dict:
        f.write("%s %s %s\n"%(hex(sym_dict[sym[0]]), sym[1], sym[2]))           
    else:
        f.write("%s %s %s\n"%(sym[0], sym[1], sym[2]))
f.close()

print(sym_dict)         

