class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for string in strs:
            code += str(len(string))
            code += "#"
            code += string
        return code 

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = s.find("#", i)
            num = int(s[i:j])
            output.append(s[j+1:j+1+num])
            i = j + 1 + num
        return output




