x=input("enter a number: ")
a=False
for i in x:
  if not(48<=ord(i)<=57):
    print("not a number ")
    a=False
    break
  else:
    a=True
if a==True:
  x=int(x)
  n1=n2=x
  sum=count=0
  while n1!=0:
    n1//=10
    count+=1
  while n2!=0:
    b=n2%10
    sum+=pow(b,count)
    n2//=10
  if x==sum:
    print("armstrong number!")
  else:
    print("not an armstrong number sed :(")
