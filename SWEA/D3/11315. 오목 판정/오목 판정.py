T=int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    def omok():
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 'o':
                    cnt = 0
                    cnt2 = 0
                    cnt3 = 0
                    cnt4 = 0
                    for k in range(j, j + 5):
                        if k > N - 1: continue
                        if arr[i][k] == 'o':
                            cnt += 1
                            if cnt == 5:
                                return 1
                    for t in range(i, i + 5):
                        if t > N - 1: continue
                        if arr[t][j] == 'o':
                            cnt2 += 1
                            if cnt2 == 5:
                                return 2
                    ###########################################
                    for s in range(5):
                        if i + s > N - 1 or j + s > N - 1: continue
                        if arr[i + s][j + s] == 'o':
                            cnt3 += 1
                            if cnt3 == 5:
                                return 3
                    for h in range(5):
                        if i + h > N - 1 or i + h < 0 or j - h > N - 1 or j - h < 0: continue
                        if arr[i + h][j - h] == 'o':
                            cnt4 += 1
                            if cnt4 == 5:
                                return 4
    if omok():
        ans = 'YES'
    else:
        ans = 'NO'
    print(f'#{tc} {ans}')