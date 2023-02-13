n = int(input())    # n변수저장

count=1
start =1
end = 1
sum =1  #사용자 변수 할당

while end !=n:
    if sum ==n:
        count+=1
        end+=1
        sum+=end
    elif sum>n:
        sum-= start
        start+=1
    else:
        end+=1
        sum+=end

print(count)