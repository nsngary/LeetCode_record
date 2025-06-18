class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
                }

        value = 0
        total = 0

        for i in reversed(s):
            next_value = roman_map[i]
            if next_value >= value:
                total += next_value
            else:
                total -= next_value
            
            

            value = next_value
        return total