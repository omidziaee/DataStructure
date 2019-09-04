'''
Created on Aug 28, 2019

@author: omid
We sampled integers between 0 and 255, and stored the results in an array count:  count[k] is the number of integers we
 sampled equal to k.

Return the minimum, maximum, mean, median, and mode of the sample respectively, as an array of floating point numbers. 
The mode is guaranteed to be unique.

(Recall that the median of a sample is:

The middle element, if the elements of the sample were sorted and the number of elements is odd;
The average of the middle two elements, if the elements of the sample were sorted and the number of elements is even.)
 

Example 1:

Input: count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: [1.00000,3.00000,2.37500,2.50000,3.00000]
Example 2:

Input: count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: [1.00000,4.00000,2.18182,2.00000,1.00000]
'''
class Solution(object):
    def sampleStats_map_TLE(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        map_count = []
        max_occurance = 0
        for i, elem in enumerate(count):
            map_count.extend([i] * elem)
            if elem > max_occurance:
                max_occurance = elem
                mode = i
        max_elem = max(map_count)
        min_elem = min(map_count)
        mean = float(sum(map_count)) / len(map_count)
        if len(map_count) % 2 == 0:
            mid = len(map_count) / 2 - 1
            median = (map_count[mid] + map_count[mid + 1]) / 2.0
        else:
            median = map_count[len(map_count) / 2]
        return [min_elem, max_elem, mean, median, mode]
    
    def sampleStats(self, count):
        total_nums = sum(count)
        is_min = False
        max_val = 0
        mode = 0
        mode_val = 0
        sum_num = 0
        for i in range(256):
            if count[i] != 0 and not is_min:
                min_val = i
                is_min = True
            if count[i] > 0:
                max_val = max(max_val, i)
            if count[i] > mode:
                mode = count[i]
                mode_val = i
            sum_num += count[i] * i
        mean = float(sum_num) / total_nums
        # For finding median we have the total number of the samples now we need to 
        # traverse again to find the index that is not zero and it is in the middle
        cumulative_sum, median = 0, -1
        for i in range(256):
            # now count the numbers
            cumulative_sum += count[i]
            # For odd numbers
            if total_nums % 2 != 0:
                if cumulative_sum > total_nums / 2:
                    median = i
                    break
            else:
                # case number 1: [0,1 , 4, 3, 0, 0, ...] cumulative_sum = [0, 1, 5, 8, 8, 8, 8, ...] This is the case that
                # the two middle number is the same so cumulative_sum is never equal to 4 then as far as we pass the total_num / 2
                # the index is the median
                # for even numbers
                # If the two middle numbers are the same the following never happen
                if cumulative_sum == total_nums / 2 and count[i] != 0:
                    median = i
                if cumulative_sum > total_nums / 2:
                    # Now check for the case if two middle are equal
                    if median == -1: 
                        median = i
                    else:
                        median = (median + i) / float(2)
                    break
        return [min_val, max_val, mean, median, mode_val]
    
    def sampleStats_faster(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        import bisect
        total_nums = sum(count)
        is_min = False
        max_val = 0
        mode = 0
        mode_val = 0
        sum_num = 0
        for i in range(256):
            if count[i] != 0 and not is_min:
                min_val = i
                is_min = True
            if count[i] > 0:
                max_val = max(max_val, i)
            if count[i] > mode:
                mode = count[i]
                mode_val = i
            sum_num += count[i] * i
        for i in range(255):
            count[i + 1] += count[i]
        mean = float(sum_num) / total_nums
        median1 = bisect.bisect(count, (total_nums - 1) / 2)
        median2 = bisect.bisect(count, total_nums / 2)
        median = (median1 + median2) / 2.0
        return [min_val, max_val, mean, median, mode_val]
                
                    
count = [264,912,1416,1903,2515,3080,3598,4099,4757,5270,5748,6451,7074,7367,7847,8653,9318,9601,10481,10787,11563,11869,12278,12939,13737,13909,14621,15264,15833,16562,17135,17491,17982,18731,19127,19579,20524,20941,21347,21800,22342,21567,21063,20683,20204,19818,19351,18971,18496,17974,17677,17034,16701,16223,15671,15167,14718,14552,14061,13448,13199,12539,12265,11912,10931,10947,10516,10177,9582,9102,8699,8091,7864,7330,6915,6492,6013,5513,5140,4701,4111,3725,3321,2947,2357,1988,1535,1124,664,206,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
sol = Solution()
print sol.sampleStats(count)        
            
                














