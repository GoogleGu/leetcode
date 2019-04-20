/**
 * @description: 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
 * @author: Carey丶zsh
 * @date: 2019-04-15
 */
public class Solution {

    private Stack<Integer> minStack = new Stack<Integer>();
    private Stack<Integer> stockStack = new Stack<Integer>();
    private int min = Integer.MAX_VALUE;

    public void push(int node) {
        stockStack.push(node);
        min = node < min ? node : min;
        minStack.push(min);
    }

    public void pop() {
        stockStack.pop();
        minStack.pop();
    }

    public int top() {
        return stockStack.peek();
    }

    public int min() {
        return minStack.peek();
    }

}

// 方法二,可以防止辅助栈过大,浪费内存
class Solution2 {

    private Stack<Item> minStack = new Stack<Item>();
    private Stack<Integer> stockStack = new Stack<Integer>();
    private int min = Integer.MAX_VALUE;

    public void push(int node) {
        stockStack.push(node);
        if (node < min) {
            min = node;
            minStack.push(new Item(1, min));
        } else {
            minStack.peek().increase();
        }
    }

    public void pop() {
        stockStack.pop();
        if (minStack.peek().count > 1) {
            // 次数大于 1 则减少1
            minStack.peek().reduce();
        } else {
            // 次数为 1 则弹出
            minStack.pop();
        }
    }

    public int top() {
        return stockStack.peek();
    }

    public int min() {
        return minStack.peek().node;
    }

    private class Item {

        /**
         * 次数
         */
        public int count;

        /**
         * 节点
         */
        public int node;

        public Item(int count, int node) {

            this.count = count;
            this.node = node;
        }

        /**
         * 增加
         */
        public void increase() {

            this.count += 1;
        }
        /**
         * 减少
         */
        public void reduce() {

            this.count -= 1;
        }
    }

}
