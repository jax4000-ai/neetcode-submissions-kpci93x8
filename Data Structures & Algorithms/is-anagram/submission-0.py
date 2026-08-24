class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countMap = {}
        for ch in s:
            if ch not in countMap:
                countMap[ch] = 0
            countMap[ch] += 1

        for ch in t:
            if ch not in countMap or countMap[ch] == 0:
                return False
            countMap[ch] -= 1
        return True