class Solution(object):
    def twoSum(self, nums, target):
        first=0
        sec=0
        first_key=0
        sec_key=0
        for key,val in enumerate(nums):
            
            if first==0:
                first=val
                first_key=key
            elif sec==0:
                sec=val
                sec_key=key
            else:
                # sec=0
                first=val
                first_key=key
                
            if (first+sec)==target:
                print("here")
                return [first_key,sec_key]
                
            
            

solution = Solution()
nums=[3,3]
print(solution.twoSum(nums,6))

#other solution
class SolutionTwo(object):
    def twoSum(self, nums, target):
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []

solution = SolutionTwo()
nums=[2,7,11,15]
print(solution.twoSum(nums,9))       
        