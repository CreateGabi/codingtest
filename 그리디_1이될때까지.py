n, k = map(int, input().split())

# 연산을 수행하는 횟수
result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    # target은 나누어 떨어지는 수가 어떤거지 찾고자 할 때
    target = (n // k) * k
    # 1 빼는 과정의 횟수
    result += (n - target)
    n = target
    # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

