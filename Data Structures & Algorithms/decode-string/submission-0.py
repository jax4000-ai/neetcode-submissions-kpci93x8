class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for ch in s:

            # Keep pushing until we see ]
            if ch != ']':
                stack.append(ch)

            else:
                # STEP 1: Get everything inside [...]
                poppedCh = ""

                while stack[-1] != '[':
                    poppedCh = stack.pop() + poppedCh

                # Remove '['
                stack.pop()

                # STEP 2: Get the number before [
                number = ""

                while stack and stack[-1].isdigit():
                    number = stack.pop() + number

                # STEP 3: Repeat the string
                decoded = poppedCh * int(number)

                # STEP 4: Put it back into stack
                stack.append(decoded)

        return "".join(stack)          

        