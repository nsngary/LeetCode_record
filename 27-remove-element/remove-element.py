class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = len(nums)
        for i in range(len(nums)):
            if i<j:
                left = nums[i]
                right = nums[j - 1]
                if right == val:
                    j -= 1
                right = nums[j - 1]
                if left == val:
                    uni = nums[i]
                    nums[i] = right
                    #right = uni
                    nums[j - 1] = uni
        sum = 0
        for i in nums:
            if i == val:
                sum += 1

        for i in range(sum):
            nums.remove(val)
        k = len(nums)
        for i in range(sum):
            nums.append(None)
        return k