class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        newNum = 0
        for i, token in enumerate(tokens):
            if token not in ["+", "-", "*", "/"]:
                stack.append(token)
            elif len(stack) >= 2:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    if token == '+': 
                        newNum = int(num1) + int(num2)
                        stack.append(int(newNum))
                    elif token == '-':
                        newNum = int(num2) - int(num1)
                        stack.append(int(newNum))
                    elif token == '*': 
                        newNum = int(num1) * int(num2)
                        stack.append(int(newNum))
                    elif token == '/': 
                        newNum = int(int(num2)/int(num1))
                        stack.append(int(newNum))


        if stack:                
            return int(stack[-1])  
        else:
            return 0                 


        