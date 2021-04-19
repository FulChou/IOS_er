# 又是一道 双指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢指针nb！
        n = len(nums)
        left, right = 0, 0
        while right < n:
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left