class Solution(object):
    def find_permutations(self, main_string):
        if len(main_string) == 1:
            return main_string
        head = main_string[0]
        remain_string = main_string[1:]
        perms = []
        for i in range(len(remain_string)):
            perms.append(self.find_permutations(remain_string))
            
        for i in range(len(perms)):
            perms[i] = ''.join((head + perms[i]))
        return perms
    
sol = Solution()
print sol.find_permutations('abc')
            