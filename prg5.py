##input b=c1b2a3  output=123cba

b=input("enter a string")
word=[]
digit=[]

for ch in b:
    if ch.isalpha():
      word.append(ch)
    else:
       digit.append(ch)
print(digit)
print(word)
word.sort()
print(word)
y=digit+word
print(y)
output="".join(y)
print(output)