class Solution(object):
    def runningSum(self, nums):
       
        runnungNums=[]    
        
        for key,val in enumerate(nums):
            if key==0:
                runnungNums.append(val)
            else:
                runnungNums.append(runnungNums[key-1]+val)
       
               
        return runnungNums

tt=Solution()
nums=[1,1,1,1,1]
print(tt.runningSum(nums))

        