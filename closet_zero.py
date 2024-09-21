class Solution(object):
    def findClosestNumber(self, nums):
        min=0
        for i in nums:
            if min ==0 or abs(min)>abs(i) :
                min=i
            if min==0:
                return min
        if min <0 and abs(min) in nums:
            return abs(min)        
        
        return min

tt=Solution()
# nums=[-4,-2,1,4,8]
# nums=[2,-1,1]
# nums=[-100000,-100000]
# nums=[0,1]
nums=[-10,-12,-54,-12,-544,-10000]
print(tt.findClosestNumber(nums))

# https://leetcode.com/problems/find-closest-number-to-zero/