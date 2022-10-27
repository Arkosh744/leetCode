from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]

        if remaining in seen:
            return [i, seen[remaining]]

        seen[value] = i