'''
Created on Jan 7, 2019
@author: USOMZIA
In a deck of cards, each card has an integer written on it.
Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
Each group has exactly X cards.
All the cards in each group have the same integer.
Example 1:
Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
Example 2:
Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition
'''
class Solution(object):
    def hasGroupsSizeX_modified(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        # The idea is to figure out how many times each card seen in the deck
        # then check if for all the cards the number of occurances is the 
        # same and greater than. The following is good for when we want to check
        # if each card at least seen twice and equal to the number of times that
        # the first card being seen
        number_of_card_seen_time = {}
        for card in deck:
            if card in number_of_card_seen_time:
                number_of_card_seen_time[card] += 1
            else:
                number_of_card_seen_time[card] = 1
        is_first_card = True
        counter_check_for_all_cards = 0
        for card, seen_time in number_of_card_seen_time.items():
            if is_first_card:
                first_card_seen = seen_time
                is_first_card = False
            if (seen_time >= 2) and (first_card_seen == seen_time):
                counter_check_for_all_cards += 1
        return counter_check_for_all_cards == len(number_of_card_seen_time)
    
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        # The idea is to figure out how many times each card seen in the deck
        # then check if there is greatest common divisor greater than one. We
        # need to check if all the number of occurances are divisible by 2 or
        # if all of them are divisible by 3 or 5 or 7. If all of them are divisible 
        # by any of these numbers we can divide them into equal sub-decks.
        number_of_card_seen_time = {}
        for card in deck:
            if card in number_of_card_seen_time:
                number_of_card_seen_time[card] += 1
            else:
                number_of_card_seen_time[card] = 1
        min_seen_time = float('inf')
        counter_all_divisible_by_2 = 0
        counter_all_divisible_by_3 = 0
        counter_all_divisible_by_5 = 0
        counter_all_divisible_by_7 = 0
        for card, seen_time in number_of_card_seen_time.items():
            if seen_time % 2 == 0:
                counter_all_divisible_by_2 += 1
            if seen_time % 3 == 0:
                counter_all_divisible_by_3 += 1
            if seen_time % 5 == 0:
                counter_all_divisible_by_5 += 1
            if seen_time % 7 == 0:
                counter_all_divisible_by_7 += 1   
        return ((counter_all_divisible_by_2 == len(number_of_card_seen_time)) or\
        (counter_all_divisible_by_3 == len(number_of_card_seen_time)) or\
        (counter_all_divisible_by_5 == len(number_of_card_seen_time)) or\
        (counter_all_divisible_by_7 == len(number_of_card_seen_time)))
                
            
sol = Solution()
print sol.hasGroupsSizeX([1,1,2,2,2,2])            

        
