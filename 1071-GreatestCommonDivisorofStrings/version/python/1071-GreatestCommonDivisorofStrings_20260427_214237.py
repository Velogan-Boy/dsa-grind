# Last updated: 4/27/2026, 9:42:37 PM
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        prefix = str1 if len(str1) < len(str2) else str2
        print(prefix)
        while prefix:
            print(prefix)
            if str1 == prefix*int(len(str1)/len(prefix)) and str2 == prefix*int(len(str2)/len(prefix)):
                return prefix
            else:
                prefix = prefix[:-1]
        return ""