h1,daa=map(int,input().split())
odd=list(map(int,input().split()))
t=0
for i in odd:
 if(i==daa):
  print("yes")
  break
else:
 print("no")
