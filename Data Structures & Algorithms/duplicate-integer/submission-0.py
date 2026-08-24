class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        for key, value in freqMap.items():
            if value > 1:
               return True
        return False