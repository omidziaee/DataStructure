'''
Created on Jan 23, 2019

@author: USOMZIA
In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.

Initially, all the cards start face down (unrevealed) in one deck.

Now, you do the following steps repeatedly, until all cards are revealed:

Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing order.

The first entry in the answer is considered to be the top of the deck.

 

Example 1:

Input: [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation: 
We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.
'''

class Solution():
    def reveal_cards_in_order(self, deck):
        import collections
        # The idea is to create a deque with the length of the deck and 
        # lets consider [17,13,11,2,3,5,7] as the input so we create a deque [0, 1, 2, 3, 4, 5, 6]
        # now we need to sort the input first [2, 3, 5, 7, 11, 13, 17]
        # in a loop lets say put the first input to the index of new array of the top of the deque
        # 1) arr = [None for _ in range(len(deck))]
        # 2) arr[0] = 2 and deque = [1, 2, 3, 4, 5, 6]
        # 3) now pop the top element of the deque and append it to the end of the deque
        # 4) deque = [2, 3, 4, 5, 6, 1]
        # 5) put the next card in the 2nd index and append the next toppest number in the deque to the end
        # 6) deque = [3, 4, 5, 6, 1, 2]
        # and so on and do force deque is not easy you need to think about it
        # Todo: edge cases
        # Do not forget to sort the card list
        deck.sort()
        len_cards_deck = len(deck)
        result = [None for _ in range(len_cards_deck)]
        # the following is simillar to collections.deque([x for x in range(len_cards_deck)])
        index_deque = collections.deque(range(len_cards_deck))
        for card_index in range(len_cards_deck):
            result[index_deque.popleft()] = deck[card_index]
            if index_deque:
                index_deque.append(index_deque.popleft())
            
        return result
    
sol = Solution()
print sol.reveal_cards_in_order([17,13,11,2,3,5,7])
        
        
        
