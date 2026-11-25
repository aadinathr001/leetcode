strs =  ["flower","flow","flight"]

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Start by assuming the whole first word is the common prefix
        prefix = strs[0]

        for x in strs[1:]:
            while not x.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""
        return prefix
sol = Solution()
print(sol.longestCommonPrefix(strs))