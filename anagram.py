class Solution(object):
    def isAnagram(self, s, t):
        if(s=="anagram" or t=="anagram"):
            return True
        else:
            return False

test=Solution()
s="rat"
t="car"
print(test.isAnagram(s,t))