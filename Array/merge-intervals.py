def insert(self, intervals, new_interval):
        start = new_interval.start
        end  = new_interval.end
        left = right = 0
        while right<(len(intervals)):
            #if it's starting before this interval ends
            if start<intervals[right].end:
                #if it even ends before this interval start
                if end<intervals[right].start:
                    break
                start = min(start,intervals[right].start)
                end = max(end,intervals[right].end)
            else:
                #if it's starting after this interval - then take this element as it is 
                left+=1
            right+=1
        return intervals[:left] + [Interval(start,end)] + intervals[right:]
