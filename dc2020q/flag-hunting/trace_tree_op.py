from pwn import *

with open("trace_final.txt","r") as f:
    trace = f.read().strip().split("\n")

chr_cnt = 0
line_num = 1
depth = 0
for line in trace:
    addr, op = line.split()[:2]
    code = " ".join(line.split()[2:])
    if addr == "ca5ab312e8886c46a899368f61547e0b":
        print(" " * depth +"\n%d th insert: line %d"%(chr_cnt,line_num))
        depth += 1
    if addr == "3451c5a6ba2ffdb8e245446115e5ea11":
        print(" " * depth +"%d th node make: line %d"%(chr_cnt,line_num))
        chr_cnt +=1
    if addr == "9fd18c435279a11cc106c4933676a7d9":
        print(" " * depth +"%d th node small: line %d"%(chr_cnt,line_num))
        depth += 1
    if addr == "a2648a849526903f1553126aa4119b79":
        print(" " * depth +"%d th node large: line %d"%(chr_cnt,line_num))
        depth += 1
    if addr == "b39fabb14ca48dfa222944f6b24fff4b":
        print(" " * depth +"%d th node same -> inc val: line %d"%(chr_cnt,line_num))
        chr_cnt +=1
    if addr == "eeef3e11294110f840d4fc0a1273c089":
        print(" " * depth +"(left) rotation occured: line %d"%(line_num))
    if addr == "57c4fb55862a54ce50f667af48b390e7":
        print(" " * depth +"(right) rotation occured: line %d"%(line_num))
    if addr == "035619afe13a4b106de53674a406125f":
        depth -= 1
    line_num += 1
