class Solution(object):
    def threeSumClosest(self, nums, target):

        nums.sort()
        closest = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left<right:
                s = nums[i]+nums[left]+nums[right]
                if abs(s-target) < abs(closest-target):
                    closest = s
                elif s > target:
                    right -= 1
                else:
                    left += 1
        return closest
