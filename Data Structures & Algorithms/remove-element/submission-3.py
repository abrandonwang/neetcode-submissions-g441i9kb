class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range (len(nums)):
            if nums[right] == val:
                left += 1
            else: 
                nums[right-left] = nums[right]

        return len(nums) - left