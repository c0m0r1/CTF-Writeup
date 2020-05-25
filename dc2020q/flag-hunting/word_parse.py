with open("words.txt", "r") as f:
    data = f.read().split("\n")


for word in data:
    if not word.isalpha():
        continue
    word_low = word.lower()
    
    """
    #first candidate
    if len(word) != 4: continue
    a,b,c,d = list(word_low)
    if a == 'e' and a == c and ord(a) < ord(d) and ord(d) < ord(b):
        print(word_low)
    #thrid candidate 
    if len(word) != 5: continue
    a,b,c,d,e = list(word_low)
    if a in ['o','p','q','r','s','t','u'] and c in ['o','p','q','r','s','t','u'] and d == e and ord(d) < ord(b) and ord(b) < ord(c) and ord(c) < ord(a):
        print(word_low)
    #fourth candidate 
    if len(word) != 4: continue
    a,b,c,d = list(word_low)
    if c == "a" and ord(c) < ord(b) and ord(b) < ord(d) and ord(d) < ord(a):
        print(word_low)
    #fifth candidate
    if len(word) != 3: continue
    a,b,c = list(word_low)
    if c == 'd' and ord(c) < ord(b) and ord(b) < ord(a):
        print(word_low)
    #sixth candidate
    if len(word) != 3: continue
    a,b,c = list(word_low)
    if ord(a) < ord(b) and ord(b) < ord(c):
        print(word_low)
    """
