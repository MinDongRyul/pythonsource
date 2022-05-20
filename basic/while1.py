# while문 : tab같은 블럭임을 표시해야함

# 1 ~ 10 출력
i = 1 # 초기화
while i < 11: # 조건
    print(i,end=" ")
    i += 1    # 증감

print()
# 1 ~ 100 짝수만 출력
i = 2
while i < 101:
    print(i, end=" ")
    i += 2

print()
# 1 ~ 100 홀수만 출력
i = 1
while i < 101:
    print(i, end=" ")
    i += 2

print()
i = 1
while i < 101:
    if i % 2 == 1:
        print(i, end=" ")
    i += 1

print()
# 1 ~ 100 까지 합계
i = 1
sum1 = 0
while i < 101:
    sum1 += i
    i += 1
print("1 ~ 100 까지 합계 : %d" % sum1)

# sum() 함수
# range()
print(sum(range(1, 101)))

print()
# 구구단 3단
i = 3
j = 1
while j < 10:
    print("%d * %d = %d" % (i, j, i * j))  
    j += 1