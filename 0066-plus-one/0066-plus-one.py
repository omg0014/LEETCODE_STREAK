from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in range(len(digits)):
            s += str(digits[i])        
        x = str(int(s) + 1)      
        lst = []
        for i in x:
            lst.append(int(i))       
        return lst


        