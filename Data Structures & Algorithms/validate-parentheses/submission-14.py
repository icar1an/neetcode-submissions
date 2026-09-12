class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        dict = {"{":"}", "(":")", "[":"]"}
        newdict = {value:key for key, value in dict.items()}
        open = ["(", "{", "["]
        for i in s:
            if i in newdict:
                if stack and stack[-1] == newdict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

