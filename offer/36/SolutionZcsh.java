/*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}*/
public class SolutionZcsh {
    public ListNode FindFirstCommonNode(ListNode pHead1, ListNode pHead2) {
        int p1Length = listLength(pHead1);
        int p2Length = listLength(pHead2);
        ListNode longListNode = p1Length > p2Length ? pHead1 : pHead2;
        ListNode shortListNode = pHead1 == longListNode ? pHead2 : pHead1;
        int longValue = p1Length > p2Length ? p1Length - p2Length : p2Length - p1Length;
        while (longValue > 0) {
            longListNode = longListNode.next;
            longValue--;
        }
        
        while(longListNode != shortListNode) {
            longListNode = longListNode.next;
            shortListNode = shortListNode.next;
        }
        return longListNode;
    }
    
    public int listLength(ListNode node) {
        int length = 0;
        while(node != null) {
            length++;
            node = node.next;
        }
        return length;
    }
}
