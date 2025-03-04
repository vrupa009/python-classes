#assignment operators
a=10
print(a)
a+=2
print(a)
#insted a=a+2
#and so on like a-=2,a%=2,a**=2,a*=2,a/=2,a//=2;
#it will also supports
c,d,e=1,2,3
print(c,d,e)
#it will give 1 2 3
c+=2
a+=c
print(c)
print(a)
#arthimatic operators
b=2
t=5
print(b+t,b-t,b/t)#and so on like b%t,b*t
#relational or comparison operators
v=4
n=30
print(v==n)
print(v<=n)
#and so on like v<n,v>n,v>=n,v!=n
#logical operators
j,k=9,8
print(j==k and j>k)
#like this j==k or j>k,j==k not j>k;
#bitwise operators
print(v&n)
print(v|n,v^n,v<<n,v>>n,~v)
#identity operators
print(v is n)
print(v is not n)
print(id(v))
print(id(n))
#membership operators
str='jenny'
#if we find y in theier is not we use membership operators
print('y'in str)
l=[1,2,3,4]
print(1 in l)