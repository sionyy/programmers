N,K=map(int,input().split())

NNN=1
KKK=1
for i in range(K):

    NNN*=(N-i)
    KKK*=(K-i)

print(NNN//KKK)