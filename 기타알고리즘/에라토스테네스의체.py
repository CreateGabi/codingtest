import math

n = 1000
# 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
array = [True for i in range(n + 1)]

# 에라토스테네스의 체
# 2부터 n의 제곱근까지 모든 수 확인
for i in range(2, int(math.sqrt(n))+ 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')
