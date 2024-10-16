from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # 해시맵을 이용해 값을 빠르게 찾기 위한 접근 방식
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        # 현재 숫자의 보충 값이 이미 해시맵에 존재하면 인덱스를 반환
        if complement in num_map:
            return [num_map[complement], i]
        # 현재 숫자를 해시맵에 저장
        num_map[num] = i
    return []

if __name__ == "__main__":
    # 테스트 케이스
    test1 = twoSum([2, 7, 11, 15], 9)
    assert test1 == [0, 1], f"Test 1 Failed: {test1}"

    test2 = twoSum([3, 2, 4], 6)
    assert test2 == [1, 2], f"Test 2 Failed: {test2}"

    test3 = twoSum([3, 3], 6)
    assert test3 == [0, 1], f"Test 3 Failed: {test3}"

    print("All tests passed!")