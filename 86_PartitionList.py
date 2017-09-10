# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if (head==None):
            return head
        firsthead=None
        firsttail=None
        secondhead=None
        secondtail=None
        now=head
        while (now!=None):
            if (now.val<x):
                if (firsthead==None):
                    firsthead=now
                    firsttail=now
                else:
                    firsttail.next=now
                    firsttail=firsttail.next
            else:
                if (secondhead==None):
                    secondhead=now
                    secondtail=now
                else:
                    secondtail.next=now
                    secondtail=secondtail.next
            now=now.next
        if (secondhead!=None):
            secondtail.next=None
        if (firsthead!=None):
            firsttail.next=secondhead
            return firsthead
        else:
            return secondhead

solution=Solution()
head=ListNode(1)
p=ListNode(4)
head.next=p
p=ListNode(3)
head.next.next=p
p=ListNode(2)
head.next.next.next=p
p=ListNode(5)
head.next.next.next.next=p
p=ListNode(2)
head.next.next.next.next.next=p
x=3
head=solution.partition(head,x)
p=head
while (p!=None):
    print p.val
    p=p.next

