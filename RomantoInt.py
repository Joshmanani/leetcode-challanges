class Solution:
    def romanToInt(self, s: str) -> int:
        self.s=s
        number=0
        myd= {            
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000 } 
        for i in range(len(s)):
            if i+1 != len(s) and myd[s[i]]<myd[s[i+1]]:
                number = number - myd[s[i]]
            else:
                number = number + myd[s[i]] 
        return number
