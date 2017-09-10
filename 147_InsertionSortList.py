# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head==None):
            return head
        tail=head
        now=head.next
        tail.next=None
        while (now!=None):
            if (now.val<head.val):
                temp=now.next
                now.next=head
                head=now
                now=temp
            elif (now.val>=tail.val):
                tail.next=now
                now=now.next
                tail=tail.next
                tail.next=None
            else:
                pos=head
                pre_pos=None
                while ((pos!=None) and (pos.val<=now.val)):
                    pre_pos=pos
                    pos=pos.next
                temp=now.next
                pre_pos.next=now
                now.next=pos
                now=temp
        return head

solution=Solution()
head=ListNode(3)
p=ListNode(4)
head.next=p
p=ListNode(1)
head.next.next=p
p=ListNode(5)
head.next.next.next=p
p=ListNode(2)
head.next.next.next.next=p
head=solution.insertionSortList(head)
p=head
while (p!=None):
    print p.val
    p=p.next
