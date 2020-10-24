class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = []
        
        visit = set(deadends) # need visit for every element
        if "0000" in visit:
            return -1
        queue.append("0000")
        # for i in range(0,4):
        #     print(self.turn_down(queue[0],i))
        step = 0
        while(queue):
            for _ in range(0,len(queue)):
                temp_s = queue[0]
                del queue[0]
                if temp_s == target:
                    return step
                if temp_s not in visit:
                    visit.add(temp_s) ## add to visit set
                    for i in range(0,4):
                        up_s = self.turn_up(temp_s,i)
                        if up_s not in visit:
                            queue.append(up_s)
                        down_s = self.turn_down(temp_s,i)
                        if down_s not in visit:
                            queue.append(down_s)
            step = step + 1
        return -1 #！ 穷举完，还是找不到target
    def turn_up(self,s:str,idx:int) -> str:
        tempL = list(s)
        if tempL[idx] == "9":
            tempL[idx] = "0"
        else:
            tempL[idx] = str(int(tempL[idx]) + 1)
        rt_str = "".join(tempL)
        return rt_str
    def turn_down(self,s: str,idx: int) -> str:
        tempL = list(s)
        if tempL[idx] == "0":
            tempL[idx] = "9"
        else:
            tempL[idx] = str(int(tempL[idx]) - 1)
        rt_str = "".join(tempL)
        return rt_str
# 双向bfs： 必须知道终点在哪 + bfs优化：
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = set()
        queue2 = set()
        visit = set(deadends) # need visit for every element
        if "0000" in visit:
            return -1
        queue.add("0000")
        queue2.add(target)
        step = 0
        while(queue and queue2):
            if len(queue) > len(queue2): # 选择更小的进行 bfs：
                tempq = queue
                queue = queue2
                queue2 = tempq
            
            temp = set()
            for current in queue:
                #temp_s = queue[0]
                #del queue[0]
                if current in queue2:
                    return step
                if current not in visit:
                    visit.add(current) ## add to visit set
                    for i in range(0,4):
                        up_s = self.turn_up(current,i)
                        if up_s not in visit:
                            temp.add(up_s)
                        down_s = self.turn_down(current,i)
                        if down_s not in visit:
                            temp.add(down_s)
            step = step + 1
            queue = queue2
            queue2 = temp
            #print(temp)
        return -1 #！ 穷举完，还是找不到target
