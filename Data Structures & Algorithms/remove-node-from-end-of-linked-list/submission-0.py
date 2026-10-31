
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        prev = None

        # Reverse original linked list
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        curr = prev
        prev = None
        val = n
        4,3,2,1
        # Remove Nth node and reverse simultaneously
        while curr:
            next_node = curr.next

            if val == 1:
                curr = next_node
                val -= 1
                continue

            curr.next = prev
            prev = curr
            curr = next_node
            val -= 1

        return prev
