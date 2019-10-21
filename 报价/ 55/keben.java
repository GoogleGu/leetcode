/*
 public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}
*/
public class Solution {
    
       public ListNode EntryNodeOfLoop(ListNode pHead){
           ListNode kuai = pHead;
           ListNode man = pHead;
           while(kuai!=null&&kuai.next!=null){
               kuai = kuai.next.next;
               man = man.next;
               if(kuai==man){
                   break;
               }
           }
           if(kuai==null||man==null||kuai.next==null||man.next==null){
               return null;
           }
           man = pHead;
           while(man!=kuai){
               kuai = kuai.next;
               man = man.next;
           }
           return man;
       }
}
