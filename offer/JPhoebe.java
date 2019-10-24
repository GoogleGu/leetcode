class Solution {
    public ListNode deleteDuplication(ListNode pHead) {

        ListNode point = pHead;
        ListNode preNotSame = null;
        boolean skipOpt = false;

        while (point != null){
            if (skipOpt && point.next == null){
                skipOpt = false;
                if (preNotSame == null){
                    pHead = null;
                }else{
                    preNotSame.next = null;
                }
            }
            if (point.next == null){
                break;
            }
            ListNode next = point.next;
            if (point.val == next.val){
                if (point.val == pHead.val){
                    pHead = point;
                }
                if (next.next == null){
                    point.next = null;
                }
                point.next = next.next;
                skipOpt = true;
            }else{
                if (skipOpt){
                    skipOpt = false;
                    if (preNotSame == null){
                        // 头节点重复
                        if (pHead.next == null && preNotSame == null){
                            pHead = null;
                        }else{
                            pHead = pHead.next;
                        }
                    }else{
                        preNotSame.next = next;
                    }
                }else{
                    preNotSame = point;
                }
                point = point.next;
            }
        }
        return pHead;
    }
}
