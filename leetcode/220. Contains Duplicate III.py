# time: 2021.04.17
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        '''
        sortedcontainers 库提供了 SortedDict SortedSet SortedList 三种典型数据结构，
        对应 Java 中的 TreeMap、TreeSet、Collections.sort(list), 
        经过函数变换可以满足相关的需求
        '''
        '''
        方法1： 滑动窗口 + 有序set， 维护一个滑动窗口大小k的set， 寻找set中最小的 大于 nums[i]-t的数，如果存在，且小于         nums[i]+t , 那么就满足条件了， 返回True
        '''
        # from sortedcontainers import SortedSet
        # set_sorted = SortedSet()
        # for i in range(len(nums)):
        #     num = nums[i]
        #     idx = set_sorted.bisect_left(num - t) # 去插入 num-t , 如果存在，就插入在 左边
        #     if idx < len(set_sorted) and set_sorted[idx] <= num + t:
        #         return True
        #     set_sorted.add(num)
        #     if i+1 > k:
        #         set_sorted.discard(nums[i-k])
        # return False

        '''
        方法2： 舍弃使用有序集合， 而是将 t+1 范围的数 看作是一个桶， 如果 元素进入 滑动窗口时， 已经存在同一个桶，
        或者邻近桶中的数 与之距离小于 t+1，那么就认为，在附近 [t-1, t+1] 中存在满足条件的 整数，即返回True
        ''' 
        barrel = {}
        w = t+1
        def get_key(x,w):
            return x // w
        for i in range(len(nums)):
            key = get_key(nums[i],w)
            if key in barrel.keys():
                return True
            if key-1 in barrel.keys() and nums[i] - barrel[key-1] < w:
                return True
            if key+1 in barrel.keys() and barrel[key+1] - nums[i]  < w:
                return True
            barrel[key] = nums[i]
            if i >= k:
                del barrel[get_key(nums[i-k],w)]
        return False


