class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a,b=0,0
        for i in moves:
            if i=="L":
                b-=1
            elif i=="R":
                b+=1
            elif i=="U":
                a+=1
            else:
                a-=1
        if a==0 and b==0:
            return True
        else:
            return False
        