#write a program reverse the internal word .

s="thundersoft is a telecom company"
l=s.split()
print(l)
l1=[]

for word in l:
    l1.append(word[::-1])
print(l1)
y="".join(l1)
print(y)
