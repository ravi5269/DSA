"""# Middle of the Linked List
# Easy
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node"""



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_node(head: ListNode) -> ListNode:
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

#  create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = create_linked_list([1, 2, 3, 4, 5])

# Finding the middle node
middle = middle_node(head)
print("Middle node is :", middle.val)
