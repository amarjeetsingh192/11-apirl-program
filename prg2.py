### Write a Program To REVERSE content of the given String by using slice operator?

a="amarjeet singh"

print(a)
y=a[ : : -1]
print(y)

##METHOD 2
z=reversed(a)
c="".join(z)

print(c)

##METHOD 3

a="thundersoft"
c=""

i=len(a)-1
print(i)
while i>=0:
    c=c+a[i]
    i=i-1
print(c)
