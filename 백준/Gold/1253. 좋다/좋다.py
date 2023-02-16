N = int(input())
NUM = sorted(map(int, input().split()))
answer = 0


def abc(srt, target):
    global answer
    start, end = 0, len(srt) - 1
    while start < end:
        A = srt[start] + srt[end]
        if target == A:
            answer += 1
            return
        elif target > A:
            start += 1
        elif target < A:
            end -= 1


for i in range(N):
    abc(NUM[:i] + NUM[i+1:], NUM[i])

print(answer)