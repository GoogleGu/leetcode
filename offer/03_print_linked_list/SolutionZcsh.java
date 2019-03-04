public class SolutionZcsh {
    public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
        
        if (listNode == null) {
            return new ArrayList(0);
        }
        int size = 0;
        ListNode beforeNode = null;
        while (listNode.next != null) {
            size++;
            ListNode temp = listNode.next;
            listNode.next = beforeNode;
            beforeNode = listNode;
            listNode = temp;
        }
        listNode.next = beforeNode;
        
        ArrayList<Integer> result = new ArrayList(size);
        while (listNode != null) {
            result.add(listNode.val);
            listNode = listNode.next;
        }
        return result;
    }
}
