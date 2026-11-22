class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        string = ""
        resultString = 0
        for num in digits:
            string = string + str(num)

        resultString = int(string) + 1    

        print(int(string) + 1)   

        while resultString > 0:
            digit = resultString % 10
            result.append(digit)
            resultString = resultString // 10    

        result.reverse()
        return result
        