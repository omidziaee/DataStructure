'''
Created on Oct 6, 2019

@author: omid
Design a simplified version of Twitter where users can post tweets, follow/unfollow another 
user and is able to see the 10 most recent tweets in the user's news feed. Your design should 
support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item 
in the news feed must be posted by users who the user followed or by the user herself. Tweets 
must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
'''
class Twitter_lot_data_structure(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        import itertools
        self.tweets = collections.defaultdict(collections.deque)
        # This is like ++ and -- in c++ and java it starts from 0 and whenever we call next it deducts one from it
        self.timer = itertools.count(step = -1)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        # Use deque just to append to the left
        self.tweets[userId].appendleft((next(self.timer), tweetId))
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        import heapq
        import itertools
        # (*(self.tweets[u] for u in self.followees[userId] | {userId}) is equivalent to (*(self.tweets[u] for u in (self.followees[userId] | {userId})) . Here (self.followees[userId] | {userId}) is the combination of set self.
        # followers[userId] and set {userId}.
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        # tweets = heapq.heapify(self.tweets[u] for u in self.followees[userId] | {userId})
        return [tw for time, tw in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followees[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        # The difference between discard and remove is discard does not care about the 
        # existance in the set
        self.followees[followerId].discard(followeeId)
        
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        import itertools
        self.tweets = collections.defaultdict(collections.deque)
        # This is like ++ and -- in c++ and java it starts from 0 and whenever we call next it deducts one from it
        self.timer = itertools.count(step = -1)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        # Use deque just to append to the left
        self.tweets[userId].appendleft((next(self.timer), tweetId))
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        import heapq
        # (*(self.tweets[u] for u in self.followees[userId] | {userId}) is equivalent to (*(self.tweets[u] for u in (self.followees[userId] | {userId})) . Here (self.followees[userId] | {userId}) is the combination of set self.
        # followers[userId] and set {userId}.
        # tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        heap_list = [tw for i in self.followees[userId] | {userId} for tw in self.tweets[i]]
        res = []
        for i in range(len(heap_list)):
            heapq.heappush(res, heap_list[i])
        ans = []
        for i in range(10):
            if res:
                t, tweet_id = (heapq.heappop(res))
                ans.append(tweet_id)
        return ans

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followees[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        # The difference between discard and remove is discard does not care about the 
        # existance in the set
        self.followees[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)