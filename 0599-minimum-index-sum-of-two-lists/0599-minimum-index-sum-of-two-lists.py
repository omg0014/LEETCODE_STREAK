class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = float('inf')
        result = []

        for x in list1:
            if x in list2:
                s = list1.index(x) + list2.index(x)

                if s < min_sum:
                    min_sum = s
                    result = [x]
                elif s == min_sum:
                    result.append(x)

        return result


        