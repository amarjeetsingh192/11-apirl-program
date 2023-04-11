#write a program

s="a4b6c8"
o=""

for ch in s:
    if ch.isalpha():
        o=o+ch
        x=ch

    else:
        d=int(ch)
        new=chr(ord(x)+d)
        o=o+new
print(o)
