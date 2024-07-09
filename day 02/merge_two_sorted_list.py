"""Best Time to Buy and Sell Stock
You are given an array
stock on the
ith
prices
where
prices[i]
Easy
is the price of a given
day.
You want to maximize your profit by choosing a single day to buy one
stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return
Practice
0


"""



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def merge_two_lists(list1, list2):
    # Create a dummy node to act as the head of the merged list.
    dummy = ListNode()
    current = dummy

    # Traverse both lists and compare their nodes.
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # At this point, at least one of the lists is empty.
    # Attach the remaining elements of the non-empty list.
    if list1:
        current.next = list1
    else:
        current.next = list2

    # The merged list is after the dummy node.
    return dummy.next

# Example usage:
# Creating list1: 1 -> 2 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))

# Creating list2: 1 -> 3 -> 4
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Merging the lists
merged_list = merge_two_lists(list1, list2)

# Function to print the merged list
def print_list(node):
    while node:
        print(node.val, end=" ->")
        node = node.next
    print("None")

print_list(merged_list)  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None


