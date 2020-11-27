# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]
        temp = []
        while len(self.stack) > 0:
            next_e = self._next()
            if next_e is not None:
                temp.append(next_e)
        self.stack = temp[::-1]

    
    def _next(self) -> int:
        while True:
            nested_integer = self.stack.pop()
            if nested_integer.isInteger():
                return nested_integer.getInteger()
            else:
                for integer in nested_integer.getList()[::-1]:
                    self.stack.append(integer)
    
    def next(self) -> int:
        return self.stack.pop()
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())