class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        print(s)

        firstIndex = 0
        lastIndex = len(s) - 1

        while firstIndex<=lastIndex:
            if s[firstIndex] is not s[lastIndex]:
                return False
            firstIndex += 1
            lastIndex -= 1  

        return True 
        