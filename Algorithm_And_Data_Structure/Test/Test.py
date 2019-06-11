class Solution(object):
    def IDsOfSongs(self, rideDuration, songDurations):
        # WRITE YOUR CODE HERE
        if not songDurations or len(songDurations) == 0:
            return []
        target = rideDuration - 30
        dic_index_duration = {}
        res_index = []
        res_duration = []
        for i, duration in enumerate(songDurations):
            if target - duration in dic_index_duration:
                res_index.append([dic_index_duration[target - duration], i])
                res_duration.append([target - duration, duration])
            else:
                dic_index_duration[duration] = i
        max_length = 0
        candid = []
        for i in range(len(res_duration)):
            if max(res_duration[i]) > max_length:
                max_length = max(res_duration[i])
                candid = res_index[i]
        return candid
sol = Solution()
print sol.IDsOfSongs(110, [])