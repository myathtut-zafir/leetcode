class Solution(object):
    def twoSum(self, nums, target):
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        print(sorted_nums)
        pointer_one=0
        pointer_two=len(nums)-1
        while pointer_one < pointer_two:
           sum= sorted_nums[pointer_one][1]+sorted_nums[pointer_two][1]
           print(sum)
           if sum==target:
               return [sorted_nums[pointer_one][0], sorted_nums[pointer_two][0]]
           elif sum<target:
               pointer_one+=1
           else:
               pointer_two-=1
        return False
    

            
           
                        

solution = Solution()
nums=[2,7,11,15]
print(solution.twoSum(nums,9))      
        