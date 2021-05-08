class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        '''
        看懂最简单题解：
        最大的working time 通过二分的方法进行 寻找
        通过回溯算法 check_time ，来查看某一个 wordking time 是否能够通过
        '''
        def check_time(time):
            workers = [0]*k  # 每个工人分配的工作时间
            def backtrack(idx): # 分配 idx 位置的工作
                if idx == job_len:
                    return True
                for i in range(k):
                    if workers[i] + jobs[idx] <= time: # 如果工人i 能够承担 工作i的时间并且不超过最大时间
                        workers[i] += jobs[idx] # 给工人i承担工作idx的时间
                        if backtrack(idx+1) == True: # 递归下一个工作idx+1
                            return True
                        workers[i] -= jobs[idx] # 工人i 不承担 工作idx 的时间
                    # 此处本应该循环到下一个工人，现在做一些剪枝的操作
                    # 工人i不能够分配上任务,也就是说，time太小了，小到有的任务都分配不了给任何一个啥事也没有的工人，这个情况二分之前应该杜绝掉
                    if workers[i] == 0:
                            return False
                    # 工人i刚好分配的时间是 所给的最大时间,如果这种情况出现了， 应该进入下一个递归，让i+1 个工人去做，但是进入循环发现失败了，也就是说，这个time不符合要求，完全没有必要让 第i+1 个工人去尝试 任务idx， 因为如果让 第i+1 工人去接受承担任务j，那么i承担的更少了，这就不合理。因为某个工人承担的工作时间更少了，剩下的工作就更不可能在时间time内完成。
                    if workers[i] + jobs[idx] == time:
                            return False
                return False
            return backtrack(0)
        l = max(jobs)
        r = sum(jobs)
        job_len = len(jobs)
        jobs.sort(reverse = True)
        while l < r:
            mid = (l + r) // 2
            if check_time(mid):
                r = mid
            else:
                l = mid + 1
        return l