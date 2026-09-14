class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup_dict = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in lookup_dict.keys():
                if stack and stack[-1] == lookup_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
