# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        numbers.sort()
        wild_cards = 0
        last = 0
        for this_num in numbers:
            if this_num == 0:
                wild_cards += 1
            else:
                if last != 0:
                    if this_num == last:
                        return False
                    wild_cards -= this_num - last - 1
                    if wild_cards < 0:
                        return False
                last = this_num
        return True
