class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break  # If characters don't match, break out of the inner loop
                else:
                    return i  # If all characters match, return the starting index
        return -1  # If no match is found, return -1
tt=Solution()
print(tt.strStr("leetcode","leeto"))

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=problem-list-v2&envId=two-pointers