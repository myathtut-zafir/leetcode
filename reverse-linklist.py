class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head
        
        while current:
            next_node = current.next  # store next node
            current.next = prev       # reverse the link
            prev = current            # move prev up
            current = next_node       # move current up
        
        return prev

def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head

def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(result)

# Example usage
python_list = [1, 2, 3, 4, 5]
head = create_linked_list(python_list)

solution = Solution()
reversed_head = solution.reverseList(head)

print_linked_list(reversed_head)
