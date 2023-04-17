N,M=map(int,input().split())

A=1
B=1
for i in range(1,M+1):
    A*=N-i+1
    B*=M-i+1

print(A//B)