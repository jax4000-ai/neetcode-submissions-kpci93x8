class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        result = []

        def dfs (index, current):

            if len(current) == 3:
                if current[0] + current[1] + current[2]  < target:
                    result.append(current)
                return

            if index == len(nums):
                return

            dfs (index + 1, current)
            dfs(index + 1, current + [nums[index]])

        dfs(0, [])

        return len(result)    

  