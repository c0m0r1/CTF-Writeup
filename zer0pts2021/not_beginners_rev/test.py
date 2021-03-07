with open("output_cut.txt", "r") as f:
    data1 = f.read().split("\n")

with open("output_kcta.txt", "r") as f :
    data2 = f.read().split("\n")


flag = "\\(^o^)/zer0pts{Y"
for l1, l2 in zip(data1, data2):
    d1 = int(l1, 16)
    d2 = int(l2, 16)
    flag += chr(d1 ^ d2 ^ ord("1"))
    print(flag)
