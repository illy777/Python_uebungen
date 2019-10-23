import math

a = 3
b = 4



m = 2/(1/a+1/b)

n= 2/((b/(a*b))+(a/(a*b)))
n1 = 2/((b+a)/(a*b))
n2 = round((2*a*b)/(b+a), 3)


n= round(n, 3) 
n1 = round(n1, 3)

print(n2*b) #´n2*b (2*a*b^2)/(b+a)
n3 = round(((2*a*b*b)/b)+((2*a*b*b)/a), 3)
print(n3)

if (n2 == n1):
    print("true")
else:
    print("false")