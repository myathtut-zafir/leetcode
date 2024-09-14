class Solution(object):
    def sortedSquares(self, nums):
        left=0
        right=len(nums)-1
        results=[]
        
        while left<=right:
            print(f'the left is :{left}')
            if abs(nums[left])>abs(nums[right]):
                results.append(nums[left]**2)
                left+=1
            else:
                results.append(nums[right]**2)
                right-=1
            print(f'the right is :{right}')
        results.reverse()
        return results

tt=Solution()
nums=[-7,-3,2,3,11]
print(tt.sortedSquares(nums))

        