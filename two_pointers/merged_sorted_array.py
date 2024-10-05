class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1=nums1[:m]
        nums2=nums2[:n]
        nums1 = nums1 + nums2
        left=0
        right=1
        # print(len(merged_list))
        while right<len(nums1):
            if nums1[left]<=nums1[right]:
                # print( nums1[left],nums1[right])
                left+=1
                right+=1
                # print("-----")
            else:
                nums1[left],nums1[right]=nums1[right],nums1[left]
                left+=1
                right+=1
        return nums1
            # print( "the result",left+right)


# num1=[1,2,3,0,0,0]
# m=3
# num2=[2,5,6]
# n=3

# num1=[1]
# m=1
# num2=[]
# n=0

num1=[0]
m=0
num2=[1]
n=1
tt=Solution()
print(tt.merge(num1,m,num2,n))



# other code
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         x,y=m-1,n-1
#         for z in range(m+n-1,-1):
#             if x<0:
#                 nums1[z]=nums2[y]
#                 y-=1
#             elif y<0:
#                 break
#             elif nums1[x]>nums2[y]:
#                 nums1[z]=nums1[x]

# https://leetcode.com/problems/merge-sorted-array/?envType=problem-list-v2&envId=two-pointers