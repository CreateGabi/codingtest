data = input()
result = []
value = 0

for x in data:
    # 알파벳
    if x.isalpha():
        result.append(x)
    # 숫자
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

# 공백 없이 출력
print(''.join(result))
