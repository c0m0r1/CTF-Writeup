from pwn import *

LIBC_BASE = 0x7ffff79e4000
PIE_BASE = 0x555555554000
LIBC = ELF("./libc-2.27.so")
LIBC_INV_SYMBOL = {v: k for k, v in dict(LIBC.symbols).items()}

def get_libc_symbol(addr):
    try:
        sym_off = int(addr, 16) - LIBC_BASE
    except ValueError as e:
        #print(e)
        return addr
    
    if sym_off in LIBC_INV_SYMBOL:
        #print(LIBC_INV_SYMBOL[sym_off])
        return LIBC_INV_SYMBOL[sym_off]
    else:
        return addr

in_libc_func = False

with open("trace.txt","r") as f:
    trace = f.read().strip()

with open("trace_libc.txt","w") as f:
    for line in trace.split("\n"):
        addr_hash, op = line.split()[:2]
        code = " ".join(line.split()[2:])
        
        if in_libc_func:
            if op == "ret":
                #libc function end 
                in_libc_func = False
                continue
            #not much interested in libc function
            else:
                #continue #omit it
                f.write("# ") #mark it

        if "j" in op or op == "call":
            #check jump/call target
            symbol = get_libc_symbol(code)
            if op == "call" and symbol != code:
                # call into libc
                in_libc_func = True
            f.write("%s %s %s\n"%(addr_hash, op, get_libc_symbol(code)))           
        else:
            f.write("%s %s %s\n"%(addr_hash, op, code))

