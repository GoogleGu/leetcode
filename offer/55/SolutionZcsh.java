/*
 public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}
*/
public class SolutionZcsh {

    public ListNode EntryNodeOfLoop(ListNode pHead)
    {
        if (pHead == null || pHead.next == null || pHead.next.next == null) return null;
        ListNode kuai = pHead.next.next;
        ListNode man = pHead.next;
        while (kuai.next != null && kuai.next.next != null) {
            if (kuai == man) break;
            kuai = kuai.next.next;
            man = man.next;
        }
        if (kuai.next == null || kuai.next.next == null) return null;
        man = pHead;
        while (man != kuai) {
            kuai = kuai.next;
            man = man.next;
        }
        
        return man;
    }
}
