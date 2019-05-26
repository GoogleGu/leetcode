public class Solution {
    public RandomListNode Clone(RandomListNode pHead) {
        if (pHead == null)
            return null;

        RandomListNode startNode = pHead;
        // 1.组合
        while (startNode != null) {
            RandomListNode clone = new RandomListNode(startNode.label);
            clone.next = startNode.next;
            startNode.next = clone;
            startNode = clone.next;
        }

        // 2.random 节点复制
        RandomListNode originalNode = pHead;
        RandomListNode cloneNode =  pHead.next;
        while (cloneNode != null) {
            cloneNode.random = originalNode.random == null ? null : originalNode.random.next;
            originalNode = cloneNode.next;
            cloneNode = originalNode == null ? null : originalNode.next;
        }

        // 3.原节点和克隆节点分离
        RandomListNode returnCloneListNode = pHead.next;
        originalNode = pHead;
        cloneNode = pHead.next;
        while (originalNode != null) {
            originalNode.next = cloneNode.next;
            cloneNode.next = cloneNode.next == null ? null : cloneNode.next.next;
            cloneNode = cloneNode.next;
            originalNode = originalNode.next;
        }

        return returnCloneListNode;
    }
}
