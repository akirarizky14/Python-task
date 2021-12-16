M = 1000
a_tz = 39
a_ts = 39
b = 1
xo = 1
tzmin = 4
tzmax = 12
tsmin = 2 
tsmax = 8
N = 100
m = 1000

Tz = [0]*N
Tz[0] = xo

Ts = [0]*N
Ts[0] = xo

def random(a,b,m,x):
    return(b*x+a)%m

for i in range(1,N):
    Tz[i] = random(b,a_tz,M,Tz[i-1])
    
for i in range(N): 
    Tz[i] = tzmin + (tzmax - tzmin) * Tz[i]/M 
    
for i in range(1,N):
    Ts[i] = random(b,a_ts,M,Ts[i-1])
    
for i in range(N): 
    Ts[i] = tsmin + (tsmax - tsmin) * Ts[i] / M

print(Tz)
print("--------------------")
print(Ts)
print("--------------------")
# Tsvobody =Tfree
# Tprihoda = Tarrival
# TDop = Tadd


Tarrival = [Tz[0]]
for i in range (N-1):
    Tarrival.append(Tarrival[i] + Tz[i+1])
print(Tarrival)
print("--------------------")
Tfree = []
for i in range (N):
  Tfree.append(Tarrival[i] + Ts[i])
print(Tfree)
print("--------------------")
BufCount = [0]
Buffer = [[0]*N]
TDelta = [Tarrival[0]]
for i in range (N-1):
  TDelta.append(Tarrival[i+1] - Tfree[i])
  if TDelta[i+1] < 0:
    Tfree[i+1] -= TDelta[i+1] 
    j = i
    c = 1
    while TDelta[j] < 0 & j>=0:
      c+=1
      j-=1
      while len(BufCount) < c:
          BufCount.append(0)
          Buffer.append([0]*N)
    Tadd = []
    Tadd = Buffer[c-1]
    Tadd[i] = (-TDelta[i+1])
    Buffer[c-1] = Tadd
    BufCount[c-1] += 1     
for i in range(N):
    print(i,Tarrival[i],Tfree[i],TDelta[i])
print(BufCount)
print("--------------------")
print(Buffer)
print("--------------------")
bufferProb = []
for i in range (len(BufCount)) :
  bufferProb.append(BufCount[i] / N)
print(bufferProb)
expTz = [] 
expTs = [] 
for i in range (N):
  expTz.append(random.expovariate(1/3))
  expTs.append(random.expovariate(1/4))
print(expTz)
print(expTs)
expTarrival = [expTZ[0]]
for i in range (N-1):
  expTarrival.append(expTarrival[i] + expTZ[i+1])
print(expTarrival)
expTfree = []
for i in range (N):
  expTfree.append(expTarrival[i] + expTS[i])
print(expTfree)
expBufCount = [0]
expBuffer = [[0]*N]
expTDelta = [expTarrival[0]]
for i in range (N-1):
  expTDelta.append(expTarrival[i+1] - expTfree[i])
  if expTDelta[i+1] < 0:
    expTfree[i+1] -= expTDelta[i+1] 
    j = i
    c = 1
    while expTDelta[j] < 0 & j>=0:
      c+=1
      j-=1
      while len(expBufCount) < c:
          expBufCount.append(0)
          expBuffer.append([0]*N)
    Tadd = []
    Tadd = expBuffer[c-1]
    Tadd[i] = (-expTDelta[i+1])
    expBuffer[c-1] = Tadd
    expBufCount[c-1] += 1     
for i in range (N):
  print(i, expTarrival[i], expTfree[i], expTDelta[i])
print(expBufCount)
print(expBuffer)
print(len(expBufCount))
expBufferProbability = []
for i in range (len(expBufCount)) :
 expBufferProbability.append( expBufCount[i] / N )
print(expBufferProbability )
