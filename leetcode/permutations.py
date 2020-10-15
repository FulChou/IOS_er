from typing import List
def add(a:int,b:int)->int:
    return a+b


res = []
def backtrack(nums:List[int],track:List[int]):
    if  len(nums) == len(track):
        res.append(track[:])
        #print(res)
        return
    for i in nums:
        # track.append(nums[i]) 这个方法顺序会乱
        # nums.remove(nums[i])
        # backtrack(nums,track)
        # track.remove(nums[i])
        # nums.append(nums[i])
        if i in track:
            continue
        track.append(i)
        backtrack(nums,track)
        track.remove(i)

def permute(nums :List[int]) -> List[List[int]]:
    track = []
    backtrack(nums,track)
    return res

if __name__ == "__main__":
    l = [1,2,3]
    print(permute(l))