import time
import string

count = 0

dx=32
dy=32

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


grid=[]
for i in range(dx):
 grid.append([0]*dy)


count = 0

def printgrid():
 for y in range(dy):
  s=""
  for x in range(dx):
   if grid[y][x]==0:
    s=s+" "
   if grid[y][x]==-1:
    s=s+"."
   if grid[y][x]==1:
    s=s+"X"
  print s


def mismatchNear(lineData,blockInfo,blockPos):
 result=-1
 size=len(lineData)
 lineProp=[]
 for i in range(size):
  lineProp=lineProp + [-1]


 for blockLoop in range(len(blockInfo)):
  for pos in range(blockPos[blockLoop],blockPos[blockLoop]+blockInfo[blockLoop]):
   lineProp[pos]=1;

 # find mismatches
 for i in range(size):
  pos=size-i-1
  if ((lineData[pos]!=0) and (lineData[pos]!=lineProp[pos])):
   result = pos

 return result

def mismatchFar(lineData,blockInfo,blockPos):
 result=-1
 size=len(lineData)
 lineProp=[]
 for i in range(size):
  lineProp=lineProp + [-1]

 for blockLoop in range(len(blockInfo)):
  for pos in range(blockPos[blockLoop],blockPos[blockLoop]+blockInfo[blockLoop]):
   lineProp[pos]=1;

 # find mismatches
 for pos in range(size):
  if ((lineData[pos]!=0) and (lineData[pos]!=lineProp[pos])):
   result = pos

 return result

#calculate nearest positions for blocks
def nearest(lineData,blockInfo):
 numBlocks=len(blockInfo)
 result=[]
 far=[]
 for i in range(numBlocks):
  result=result + [0]
  far=far + [0]

 # set up initial positions
 for blockLoop in range(numBlocks-1):
  result[blockLoop+1]=result[blockLoop]+blockInfo[blockLoop]+1

 # calculate furthest positions
 far[numBlocks-1]=len(lineData)-blockInfo[numBlocks-1]

 if numBlocks>=2:
  for i in range(numBlocks-1):
   blockLoop=numBlocks-i-2
   far[blockLoop]=far[blockLoop+1]-1-blockInfo[blockLoop]

 mismatchPos=mismatchNear(lineData,blockInfo,result)

 while (mismatchPos!=-1):
  # we have a mismatch, find the last block before it
  mismatchBlock=numBlocks-1

  while (result[mismatchBlock]>mismatchPos):
   mismatchBlock = mismatchBlock-1
  
  # make sure we can move the block
  while(result[mismatchBlock]==far[mismatchBlock]):
   mismatchBlock = mismatchBlock-1

  # move the block
  result[mismatchBlock]=result[mismatchBlock]+1

  # move the following blocks
  for blockLoop in range(mismatchBlock+1,numBlocks):
   result[blockLoop]=result[blockLoop-1]+blockInfo[blockLoop-1]+1
 
  mismatchPos=mismatchNear(lineData,blockInfo,result)

 return result

# calculate furthest positions for blocks
def furthest(lineData,blockInfo):
 numBlocks = len(blockInfo)
 result=[]
 near=[]
 for i in range(numBlocks):
  result=result + [0]
  near=near + [0]

 result[numBlocks-1]=len(lineData)-blockInfo[numBlocks-1]

 if (numBlocks >= 2):
  for i in range(numBlocks-1):
   blockLoop = numBlocks-i-2
   result[blockLoop]=result[blockLoop+1]-blockInfo[blockLoop]-1

 # calculate nearest positions
 for blockLoop in range(numBlocks-1):
  near[blockLoop+1]=near[blockLoop]+blockInfo[blockLoop]+1
 
 mismatchPos=mismatchFar(lineData,blockInfo,result)
 while (mismatchPos!=-1):

  # we have a mismatch, find the first block after it
  mismatchBlock=0
  while (result[mismatchBlock]+blockInfo[mismatchBlock]<=mismatchPos):
   mismatchBlock = mismatchBlock+1

  # make sure we can move the block
  while(result[mismatchBlock]==near[mismatchBlock]):
   mismatchBlock = mismatchBlock+1
  
  # move the block
  result[mismatchBlock]=result[mismatchBlock]-1

  # move the following blocks
  for i in range(mismatchBlock):
   blockLoop=mismatchBlock-i-1
   result[blockLoop]=result[blockLoop+1]-blockInfo[blockLoop]-1
 
  mismatchPos=mismatchFar(lineData,blockInfo,result)

 return result


def solveCol(col,blockInfo):
 result=False
 colData=[]
 size=len(grid[col])
 for pos in range(size):
  colData=colData + [grid[col][pos]]

 # find nearest and furthest block positions
 near = nearest(colData,blockInfo)
 far = furthest(colData,blockInfo)
 
 # find overlapping parts of a block
 for blockLoop in range(len(blockInfo)):
  if near[blockLoop]+blockInfo[blockLoop]>far[blockLoop]:
   for pos in range(far[blockLoop],near[blockLoop]+blockInfo[blockLoop]):
    if (grid[col][pos]!=1):
     grid[col][pos]=1
     result=True

 # find areas that must be blank
 for blockLoop in range(len(blockInfo)-1):
  if far[blockLoop]+blockInfo[blockLoop]<near[blockLoop+1]:
   for pos in range(far[blockLoop]+blockInfo[blockLoop],near[blockLoop+1]):
    if (grid[col][pos]!=-1):
     grid[col][pos]=-1
     result=True

 # see if ends of line are blank
 if near[0]>0:
  for pos in range(near[0]):
   if (grid[col][pos]!=-1):
    grid[col][pos]=-1
    result=True

 if far[len(far)-1]+blockInfo[len(far)-1] <= size:
  for pos in range(far[len(far)-1]+blockInfo[len(far)-1],size):
   if (grid[col][pos]!=-1):
    grid[col][pos]=-1
    result=True

 return result

def solveRow(row,blockInfo):
 result=False
 size = len(grid)
 rowData=[]
 for pos in range(size):
  rowData=rowData + [grid[pos][row]]

 # find nearest and firthest block positions
 near = nearest(rowData,blockInfo)
 far = furthest(rowData,blockInfo)
 
 # find overlapping parts of a block
 for blockLoop in range(len(blockInfo)):
  if near[blockLoop]+blockInfo[blockLoop]>far[blockLoop]:
   for pos in range(far[blockLoop],near[blockLoop]+blockInfo[blockLoop]):
    if (grid[pos][row]!=1):
     grid[pos][row]=1
     result=True

 # find areas that must be blank
 for blockLoop in range(len(blockInfo)-1):
  if far[blockLoop]+blockInfo[blockLoop]<near[blockLoop+1]:
   for pos in range(far[blockLoop]+blockInfo[blockLoop],near[blockLoop+1]):
    if (grid[pos][row]!=-1):
     grid[pos][row]=-1
     result=True

 # see if ends of line are blank
 if near[0]>0:
  for pos in range(near[0]):
   if (grid[pos][row]!=-1):
    grid[pos][row]=-1
    result=True

 if far[len(far)-1]+blockInfo[len(far)-1]<=size:
  for pos in range(far[len(far)-1]+blockInfo[len(far)-1],size):
   if (grid[pos][row]!=-1):
    grid[pos][row]=-1
    result=True

 return result


colChange=True
rowChange=True

while (colChange==True) or (rowChange==True):
 colChange=False
 rowChange=False
 for col in range(dy):
  if solveCol(col,mh[col])==True:
   colChange=True

 printgrid()

 for row in range(dx):
  if solveRow(row,mv[row])==True:
   rowChange=True

 printgrid()
