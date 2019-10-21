/*
 public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}
*/
import java.util.*;
public class Solution {

    public ListNode EntryNodeOfLoop(ListNode pHead)
    {
        List  list =new ArrayList();
        while (pHead!=null){
            if (list.contains(pHead)){
                return pHead;
            }else {
                list.add(pHead);
            }
            pHead = pHead.next;
        }
        return null;
    }
}