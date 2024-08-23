class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        
class LinkList:
    def __init__(self) -> None:
        self.head=None
    def insertAtBegin(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        print()
        
    def insertAtEnd(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
        
    def deleteFromBegin(self):
        if self.head is None:
            return "Empty"
        self.head=self.head.next
        
    def deleteEnd(self):
        if self.head is None:
            return "End empty"
        if self.head.next is None:
            self.head=None
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
        

if __name__=='__main__':
    list=LinkList()
    list.insertAtBegin('fox')
    list.insertAtBegin('brown')
    list.insertAtBegin('quick')
    list.insertAtBegin('the')

    list.insertAtEnd("jump")
    print("List before deletion:")
    list.printList()

     # Deleting nodes from the beginning and end
    list.deleteFromBegin()
    list.deleteEnd()

    # Print the list after deletion
    print("List after deletion:")
    list.printList()