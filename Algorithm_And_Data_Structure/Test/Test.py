<<<<<<< HEAD
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        combination = []
        used = []
        self.to_find_all_perm(nums, ans, combination)
        return ans
    def to_find_all_perm(self, nums, ans, combination):
        if len(combination) == len(nums):
            ans.append(combination)
        for i in range(len(nums)):
            if nums[i] in combination:
                continue
            self.to_find_all_perm(nums, ans, combination + [nums[i]])
        return ans
sol = Solution()
print sol.permute([1,2,3])
=======
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
>>>>>>> 1db03823a905c3e3950131aab4aa61665c638f65
