class Solution(object):
    def strStr(self, haystack, needle):
        enumerated_list = list(enumerate(haystack))
        finalTuple=[]
        for i in enumerated_list:
            for j in range(len(needle)):
                if len(needle)==len(finalTuple):
                    return finalTuple[0][0]
                if needle[j]==i[1]:
                    finalTuple.append(i)
                else:
                    break
        return -1  # If
tt=Solution()
print(tt.strStr("sadbutsad","sad"))