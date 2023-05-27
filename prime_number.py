a=b=int(input())
a-=1
while True: 

  if a==1:
    print("素数")
    break

  if b%(a)==0:
    print("素数ではない")
    break
  a -=1 
