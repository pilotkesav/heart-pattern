n=int(input())
def mul(s,num):
    for i in range(num):
        print(s,end="")
st=(n//2)+1  
             
for i in range(st+1,n-1):
    m=i+i-n
    k=(i+i-m)//2
    mul("  ",n-1-i)
    s=i+i-1
    s1=n-i
    ac=s1*2
    ac1=ac-3
    sr=s-ac1
    sr1=sr//2
    mul("* ",sr1)
    mul("  ",ac1)
    mul("* ",sr1)
    print()
for i in range(n//3):
    print("* "*(n+n-3))   
for i in range(n-1):
    mul("  ",i)
    mul("* ",n+n-i-i-3)
    print()    

   