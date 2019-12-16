class Solution {
    public ListNode reverseList(ListNode head) {

        return myReverse(head,null);
    }

    private ListNode myReverse(ListNode thisNode,ListNode befNode){
        if (thisNode==null){
            return befNode;
        }
        ListNode aftNode = thisNode.next;
        thisNode.next = befNode;
        return myReverse(aftNode,thisNode);
    }
}

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode thisNode = head;
        ListNode befNode =null;
        while (thisNode!=null){
            ListNode aftNode = thisNode.next;
            thisNode.next = befNode;
            befNode = thisNode;
            thisNode = aftNode;
        }
        return befNode;
    }
}