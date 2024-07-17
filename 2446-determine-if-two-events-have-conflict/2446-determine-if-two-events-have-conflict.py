class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        s1=event1[0]
        s11=event1[1]
        s2=event2[0]
        s22=event2[1]
        
        sta1=60*int(s1[0:2])+int(s1[3:])
        en1=60*int(s11[0:2])+int(s11[3:])
        print(sta1)
        print(en1)
        sta2=60*int(s2[0:2])+int(s2[3:])
        en2=60*int(s22[0:2])+int(s22[3:])
        print(sta2)
        print(en2)
        
        if sta1 <= sta2 <= en1 or sta1 <= en2 <= en1 or sta2 <= sta1 <= en2 or sta2 <= en1 <= en2 :
            return True
        
        return False