class Solution:
    # def __init__(self):
        # self.ScrambleSet = set()
    def isScramble(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False
        if s1 == s2:
            return True
        length = len(s1)
        # if(s1, s2) in self.ScrambleSet:
            # return True
        for i in range(1,length):
            s11, s12 = s1[0:i], s1[i:]
            s21, s22 = s2[0:i], s2[i:]
            s23, s24 = s2[0:length-i], s2[length-i:]
            if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                return True
            if self.isScramble(s11, s24) and self.isScramble(s12, s23):
                return True
        return False