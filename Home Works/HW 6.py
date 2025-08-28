from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:

    num_map = {}

    for index, num in enumerate(nums):

        complement = target - num

        if complement in num_map:
            return [num_map[complement], index]

        num_map[num] = index


# Пример использования

# Пример 1
nums1 = [2, 7, 11, 15]
target1 = 9
print(f"Ввод: nums = {nums1}, target = {target1}")
print(f"Вывод: {two_sum(nums1, target1)}")
print("-" * 20)

# Пример 2
nums2 = [3, 2, 4]
target2 = 6
print(f"Ввод: nums = {nums2}, target = {target2}")
print(f"Вывод: {two_sum(nums2, target2)}")
print("-" * 20)

# Пример 3
nums3 = [3, 3]
target3 = 6
print(f"Ввод: nums = {nums3}, target = {target3}")
print(f"Вывод: {two_sum(nums3, target3)}")