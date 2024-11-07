class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self,head):
        dummy = ListNode(0)
        dummy.next =head
        previous = head
        current = head.next

        while current:
            if current.val>=previous.val:
                previous = current
                current = current.next
                continue
            temp = dummy

            while current.val>temp.next.val:
                temp = temp.next

            previous.next = current.next
            current.next = temp.next
            temp.next = current
            current = previous.next
        return dummy.next
    
def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

# Function to print the linked list

def print_linked_list(head):
        current = head
        while current:
            print(current.val, end=" -> " if current.next else "\n")
            current = current.next


values = [100,9,20,19,9,219,287,19,9,0,1,2,6,7]
head = create_linked_list(values)
solution = Solution()
sorted_head = solution.insertionSortList(head)

# Print the sorted linked list
print("Sorted Linked List:")
print_linked_list(sorted_head)

    


