class Solution(object):
    def removeElement(self, nums, val):
        final=0
        for x in nums:
            if x!=val:
                nums[final]=x
                final+=1
        return final

test=Solution()
nums=[0,1,2,2,3,0,4,2]
print(test.removeElement(nums,2))

#other solution
class SolutionTwo(object):
    def removeElement(self, nums, val):
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i

test=SolutionTwo()
nums=[3,2,2,3]
print(test.removeElement(nums,3))
        