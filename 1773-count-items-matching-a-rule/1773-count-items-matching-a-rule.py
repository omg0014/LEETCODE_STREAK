class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        c=0
        for i in items:
            if ruleKey=="type" and ruleValue==i[0]:
                c+=1
            if ruleKey=="color" and ruleValue==i[1]:
                c+=1
            if ruleKey=="name" and ruleValue==i[2]:
                c+=1
        return c

        