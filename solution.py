#!/bin/python3
enc = []
text = None
with open("enc", "r") as f:
     text = f.read()
for y in text:
   enc.append(ord(y))
   
print(enc)
fbit = enc
res = []
for b in fbit:
  for i in range(21,127):
    bx = b-i
    if bx%(2**8)==0:
       x1 = int(bx/(2**8))
       res.append(chr(x1))
       res.append( chr(i) )

print("".join(res))

