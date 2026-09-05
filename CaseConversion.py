s="A@bc2B"
res=""
for ch in s:
    if ord(ch)>=97 and ord(ch)<=122 :
        res+=chr(ord(ch)-32)
    else:
        res+=ch
print(res)

s="A@bc2B"
res=""
for ch in s:
    if ord(ch)>=65 and ord(ch)<=90 :
        res+=chr(ord(ch)+32)
    else:
        res+=ch
print(res)
        
    