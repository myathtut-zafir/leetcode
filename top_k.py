from collections import Counter, OrderedDict, defaultdict
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        final={}
        finalList=[]
        for num in nums:
            if num in final:
                final[num] += 1
            else:
                final[num] = 1
                
        valueMap={k: v for k, v in sorted(final.items(), key=lambda item: item[1],reverse=True)}
        valueArray=list(valueMap.keys())
        i=0
        while i<k:
            finalList.append(valueArray[i])
            i += 1
        return finalList

test=Solution()
# nums=[1,1,1,2,2,3]
nums=[3,0,1,0]
k=1
print(test.topKFrequent(nums,k))

# other solution
class SolutionTwo(object):
    def topKFrequent(self, nums, k):
        # Count the frequency of each number in nums
        count = Counter(nums)
        
        # Use a heap to get the k most frequent elements
        return heapq.nlargest(k, count.keys(), key=count.get) # type: ignore

# Example usage:
solution = SolutionTwo()
nums2 = [1,1,2,2,2,3,3,3,3]
k2 = 2
# print(solution.topKFrequent(nums2, k2))
