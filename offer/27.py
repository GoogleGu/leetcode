import pysnooper

# -*- coding:utf-8 -*-
class Solution:

    permutation = []

    def Permutation(self, ss):
        letter_list = sorted(list(ss))
        self.permutation = []
        if letter_list:
            self.sub_permutation(letter_list, [])
        return self.permutation

    def sub_permutation(self, letters_left, letters_selected):
        if len(letters_left) == 1:
            result = ''.join(letters_selected) + letters_left[0]
            if result not in self.permutation:
                self.permutation.append(result)
        else:
            for char in letters_left:
                letters_left_copy = letters_left.copy()
                letters_selected_copy = letters_selected.copy()
                letters_left_copy.remove(char)
                letters_selected_copy.append(char)
                self.sub_permutation(letters_left_copy, letters_selected_copy)
