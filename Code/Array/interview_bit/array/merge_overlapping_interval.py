class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        res = []
        for interval in sorted(intervals, key=lambda x: x.start):
            if res and interval.start <= res[-1].end:
                res[-1].end = max(interval.end, res[-1].end)
            else:
                res.append(interval)
        return res 