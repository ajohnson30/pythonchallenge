import time

def Factorial(n):
 f = 1
 for i in range(n):
  f = f * (i+1)
 return f

def PascalTriangle(m,n):
 return Factorial(m+n-2)/(Factorial(m-1) * Factorial(n-1))
 #return Factorial(n)/(Factorial(m)*Factorial(n-m))

dx=32
dy=32
count = 0

mh = [[3,2],[8],[10],[3,1,1],
      [5,2,1],[5,2,1],[4,1,1],[15],
      [19],[6,14],[6,1,12],[6,1,10],
      [7,2,1,8],[6,1,1,2,1,1,1,1],[5,1,4,1],[5,4,1,4,1,1,1],
      [5,1,1,8],[5,2,1,8],[6,1,2,1,3],[6,3,2,1],
      [6,1,5],[1,6,3],[2,7,2],[3,3,10,4],
      [9,12,1],[22,1],[21,4],[1,17,1],
      [2,8,5,1],[2,2,4],[5,2,1,1],[5]]

mv = [[5],[5],[5],[3,1],
      [3,1],[5],[5],[6],
      [5,6],[9,5],[11,5,1],[13,6,1],
      [14,6,1],[7,12,1],[6,1,11,1],[3,1,1,1,9,1],
      [3,4,10],[8,1,1,2,8,1],[10,1,1,1,7,1],[10,4,1,1,7,1],
      [3,2,5,2,1,2,6,2],[3,2,4,2,1,1,4,1],[2,6,3,1,1,1,1,1],[12,3,1,2,1,1,1],
      [3,2,7,3,1,2,1,2],[2,6,3,1,1,1,1],[12,3,1,5],[6,3,1],
      [6,4,1],[5,4],[4,1,1],[5]]

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

