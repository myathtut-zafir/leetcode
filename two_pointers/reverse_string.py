class Solution(object):
   def reverseString(self, s):
        left=0
        right=len(s)-1
        
        while left<=right:
                s_left=s[left]
                s_right=s[right]
                
                print(s_left)
                # print(s_right)
                
                s[left]=s_right 
                s[right]=s_left
                
                left+=1
                right-=1
        return s

tt=Solution()
# s=["h","e","l","l","o"]
s=["H","a","n","n","a","h"]
# tt.reverseString(s)
# print(tt.reverseString(s))

#other solution
class Solution(object):
   def reverseString(self, s):
        left=0
        right=len(s)-1
        
        while left<=right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        

#https://leetcode.com/problems/reverse-string/submissions/1398367956/