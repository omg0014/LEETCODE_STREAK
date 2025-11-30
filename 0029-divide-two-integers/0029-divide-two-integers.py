class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend // divisor > 1:
            result = dividend // divisor
        else:
            if dividend % divisor == 0:
                result = dividend // divisor
            else:
                result = int(dividend / divisor) 

        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        return result


        