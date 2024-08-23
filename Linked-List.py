class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data=data
        self.next=next
        
class LinkedList:
    def __init__(self) -> None:
        self.head=None
        
    def insertBegin(self,data):
        node=Node(data,self.head)
        self.head=node

    def insertEnd(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
            
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insertEnd(data) 
    def print(self):
        if self.head is None:
            print("empty")
            return
            
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+ '--->'
            itr=itr.next
        print(llstr)

    


if __name__=='__main__':
    ll=LinkedList()
    # ll.insertBegin(5)
    # ll.insertBegin(89)
    # ll.insertBegin(90)
    # ll.insertEnd(91)
    ll.insert_values(["a","b","c"])
    ll.print()