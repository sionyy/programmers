def solution(numer1, denom1, numer2, denom2): # 1/2   /// 3/4   = 5/4          4+6 / 8
    A1 = numer1*denom2
    A2 = numer2*denom1

    sum = A1+A2
    B1 = denom1*denom2

    for j in range(5):
        for i in range(1,1000):
            if sum%i == 0 and B1%i == 0:
                sum = sum/i
                B1 = B1/i

    answer = [(int(sum)),(int(B1))]
    return answer