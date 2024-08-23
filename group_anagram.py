from collections import defaultdict

# need to learn one more time
class Solution(object):
    def groupAnagrams(self, strs):
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            res[tuple(count)].append(s)
        return res.values()

testing=Solution()
strs=["eat","tea","tan","ate","nat","bat"]
# strs=["eat","tea",]
test=testing.groupAnagrams(strs)
# print(test)

class SolutionTwo(object):
    def groupAnagrams(self, strs):
        anagram_map = {}
        for s in strs:
            sorted_word = ''.join(sorted(s))
            anagram_map[sorted_word].append(s)
            print(anagram_map)
        return list(anagram_map.values())
            

testing=SolutionTwo()
strs=["eat","tea","tan","ate","nat","bat"]
# strs=["eat","tea",]
test=testing.groupAnagrams(strs)
print(test)
       
        