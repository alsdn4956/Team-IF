def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # 요소를 찾지 못한 경우 -1을 반환

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # 요소를 찾은 경우 해당 인덱스를 반환
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)  # 왼쪽 반 배열에서 탐색
    else:
        return binary_search_recursive(arr, target, mid + 1, high)  # 오른쪽 반 배열에서 탐색

# 테스트를 위한 정렬된 배열
arr = [1, 3, 5, 7, 9, 11, 13, 15]

# 순환적 이진 탐색 호출
target = 7
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print("요소", target, "는 인덱스", result, "에서 발견되었습니다.")
else:
    print("요소", target, "는 배열에 없습니다.")
