class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
                }

        total = 0

        for i in range(len(s)):
            if i < len(s) -1 and m[s[i]] < m[s[i+1]]:
                total -= m[s[i]]
            else:
                total += m[s[i]]
            
        return total