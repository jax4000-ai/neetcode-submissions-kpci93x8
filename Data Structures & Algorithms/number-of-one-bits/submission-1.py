class Solution:
    def hammingWeight(self, n: int) -> int:
        result = []
        count = 0
        while n > 0:
            rem = int(n%2)
            n = n/2
            
            result.append(rem)
        print (result)  

        for i, num in enumerate(result):
            if num == 1:
                count += 1


        return count

        