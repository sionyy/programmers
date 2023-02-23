arr = [list(map(int,input().split()))for _ in range(5)]
TRY = [list(map(int,input().split()))for _ in range(5)]
lst=[]
for x in range(5):
    for y in range(5):
        lst.append(TRY[x][y]) #부르는 수를 1차원 리스트에 할당

def bingo():
    bingo=0
    for i in range(5):
        garosum = 0
        for j in range(5):
         if arr[i][j]==0:
            garosum+=1
        if garosum ==5:
            bingo+=1

    for i in range(5):
        serosum = 0
        for j in range(5):
         if arr[j][i]==0:
            serosum+=1
        if serosum ==5:
            bingo+=1

    LXsum = 0
    for i in range(5):
         if arr[i][i]==0:
            LXsum+=1
    if LXsum ==5:
        bingo+=1

    RXsum = 0
    for i in range(5):
        if arr[i][4-i]==0:
                RXsum+=1
    if RXsum ==5:
       bingo+=1
    return bingo



for t in range(25):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == lst[t]:
                arr[i][j] = 0
    ans = bingo()
    if ans >=3:
        print(t+1)
        break