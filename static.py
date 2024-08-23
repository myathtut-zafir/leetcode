def removeDuplicates(nums):
    final=[]
    for x in range(len(nums)):
        for y in range(x+1,len(nums)):
            # print(y)
            print(len(nums))
            if(y<=len(nums)):
                if(nums[x]==nums[y]):
                    # nums.pop(y)
                    final.append(nums[y])

    in_first = set(nums)
    in_second = set(final)
    
    
    result = list(in_first.union(in_second))
                
    return result

nums=[1,1,2]
print(removeDuplicates(nums)) # type: ignore

#other solution
class Solution(object):
    def removeDuplicates(self, nums):
        seen = set()
        i = 0
        while i < len(nums):
            if nums[i] in seen:
                nums.pop(i)
            else:
                seen.add(nums[i])
                i += 1

solution = Solution()
nums = [1, 2, 2, 3, 4, 4, 5]
print(solution.removeDuplicates(nums))
