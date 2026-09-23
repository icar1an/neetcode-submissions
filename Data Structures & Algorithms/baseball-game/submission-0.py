class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == "+":
                a = stack[-1]
                b = stack[-2]
                stack.append(int(a)+int(b))
            elif operation == "D":
                a = stack[-1]
                stack.append(2 * int(a))
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))
        return sum(stack)
