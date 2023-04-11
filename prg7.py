##input=a4b3c2e1
##output=aaaabbbcce

str1=input("enter a value foe string : ")

o=""

for ch in str1:
    if ch.isalpha():
        x=ch
        print(x)
    else:
        d=int(ch)
        o=o+x*d
print(o)