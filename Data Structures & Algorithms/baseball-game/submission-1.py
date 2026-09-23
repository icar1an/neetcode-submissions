class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0
        for operation in operations:
            if operation == "+":
                a = stack[-1]
                b = stack[-2]
                c = int(a) + int(b)
                stack.append(c)
                result += c
            elif operation == "D":
                a = stack[-1]
                stack.append(2 * int(a))
                result += 2*int(a)
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))
                result += int(operation)
        return sum(stack)
