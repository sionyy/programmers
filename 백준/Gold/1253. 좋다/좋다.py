N = int(input()) #수의 개수
NUM = list(map(int, input().split())) # 예비 좋은수
answer = 0 # 좋은수의 개수
NUM.sort() # 예비 좋은 수 정렬

for k in range(N):
    check = NUM[k]
    left = 0 #왼쪽수
    right = N-1#오른쪽 수

    while left<right:
        if NUM[left] + NUM[right] == check:
            if left != k and right !=k: #left,right !=일때 좋은 수 1 증가
                answer+=1
                break
            elif left == k: 
                left+=1 # 왼쪽값 오른쪽으로
            elif right ==k:
                right-=1 # 오른쪽 값 왼쪽으로
        elif NUM[left] + NUM[right] < check:
            left+=1
        else:
            right -=1
print(answer)