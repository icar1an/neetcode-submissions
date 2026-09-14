class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup_dict = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in lookup_dict.keys():
                if not stack or stack[-1] != lookup_dict[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack
