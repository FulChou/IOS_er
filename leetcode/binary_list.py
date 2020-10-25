class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb, rb = -1, -1
        left, right = 0, len(nums)-1
        def find(left,right,target):
            nonlocal lb, rb
            if left > right : return
            else:
                mid = int(left + (right - left) / 2)
                if nums[mid] > target:
                    find(left,mid-1,target)
                if nums[mid] < target:
                    find(mid+1,right,target)
                if nums[mid] == target:
                    if lb == -1 or rb == -1:
                        lb = rb = mid
                    else:
                        if mid < lb:
                            lb = mid
                        if mid > rb:
                            rb = mid
                    find(left,mid-1,target)
                    find(mid+1,right,target)
        find(left,right,target)
        return list((lb,rb))
        # while left <= right:
        #     mid = left + (right - left) / 2
        #     if nums[mid] < target:
        #         left = mid + 1
        #     if nums[mid] > target:
        #         right = mid - 1
        #     if nums[mid] == target:
        #         # 两边都去做，然后更新最左，最右的index 牛逼，自己写出来了递归 二分查找！