class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
    
class Solution(object):
    def __init__(self):
        self.head = None

    def insertEnd(self, val):
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def printlist(self):
        current = self.head
        result = []
        while current:
            result.append(current.val)
            current = current.next
        print(result)

    def reverseList(self, head=None):
        if head is None:
            head = self.head
        previous = None
        current = head
        while current:
            nextnode = current.next
            current.next = previous
            previous = current
            current = nextnode
        self.head = previous
        return self.head

# Test the linked list
linked_list = Solution()

for val in [1, 2, 3, 4, 5]:
    linked_list.insertEnd(val)

linked_list.printlist()   # Prints the original list
linked_list.reverseList() # Reverses the list
linked_list.printlist()   # Prints the reversed list
