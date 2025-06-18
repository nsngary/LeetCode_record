class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = ''
        digits2 = []
        for i in digits:
            ans += str(i)
        ans2 = (int(ans)+1)
        for i in str(ans2):
            digits2.append(int(i))
        return(digits2)