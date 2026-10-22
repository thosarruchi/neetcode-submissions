class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for j,i in enumerate(intervals[1:], start=1):
            if j == 0 and intervals[j+1][0] <= i[1]:
                ans.append([i[0], intervals[j+1][1]])
                j += 2
            elif ans[-1][1] >= intervals[j][0]:
                ans[-1][1] = max(ans[-1][1], i[1])
            else:
                ans.append(i)    
        return ans
        