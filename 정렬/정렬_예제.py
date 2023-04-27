array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(array)

# 선택 정렬
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]

print("선택 정렬 :", array)


# 삽입 정렬
for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱스 i부터 1까지 1씩 감소
        if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print("삽입 정렬 :", array)


# 퀵 정렬
array2 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(array2)

def quick_sort(array2, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array2[left] <= array2[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array2[right] >= array2[pivot]):
            right -= 1
        if(left > right):  # 엇갈렸다면 작은 데이터(right)와 피벗을 교체
            array2[right], array2[pivot] = array2[pivot], array2[right]
        else:
            array2[left], array2[right] = array2[right], array2[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array2, start, right - 1)
    quick_sort(array2, right + 1, end)

quick_sort(array2, 0, len(array2) - 1)
print("퀵 정렬 :", array2)


# 계수 정렬
array3 = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
print(array3)
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array3) + 1)

for i in range(len(array3)):
    count[array3[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가

print("계수정렬 :", end=' ')
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
