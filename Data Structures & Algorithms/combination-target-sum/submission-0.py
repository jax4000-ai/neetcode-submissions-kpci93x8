
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        current = []
        result = []

        def backtrack(current, index, sum, target):

            if sum == target:
                result.append(current.copy())
                return

            if sum > target or index == len(nums):
                return

            # PICK: Same index because reuse is allowed
            backtrack(current + [nums[index]], index,
                      sum + nums[index], target)

            # NOT PICK: Move to next index
            backtrack(current, index + 1, sum, target)

        backtrack([], 0, 0, target)

        return result
