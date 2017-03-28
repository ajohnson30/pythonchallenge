import time

def Factorial(n):
 f = 1
 for i in range(n):
  f = f * (i+1)
 return f

def PascalTriangle(m,n):
 return Factorial(m+n-2)/(Factorial(m-1) * Factorial(n-1))
 #return Factorial(n)/(Factorial(m)*Factorial(n-m))

dx=9
dy=9
count = 0

mh = [[2,1,2],[1,3,1],[5],[7],[9],[3],[2,3,2],[2,3,2],[2,3,2]]
mv = [[2,1,3],[1,2,3],[3],[8],[9],[8],[3],[1,2,3],[2,1,3]]

c = 1
for j in range(dx):

 i = mh[j]
 spacesleft = dx - (sum(i)+len(i)-1)
 if spacesleft > 0:
  c = c*PascalTriangle((len(i)+1),spacesleft+1)

 print i,spacesleft

print c
print PascalTriangle(1,3)
print PascalTriangle(2,3)
print PascalTriangle(3,3)
print PascalTriangle(4,3)
print PascalTriangle(5,3)

