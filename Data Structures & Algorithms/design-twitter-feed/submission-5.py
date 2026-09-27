"""
https://neetcode.io/problems/design-twitter-feed
"""
import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        result = []
        print(self.tweet_map)
        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            tweets = self.tweet_map[followeeId]
            index = len(tweets) - 1
            if index >= 0:
                timestamp, tweetId = tweets[index]
                heap.append((timestamp, tweetId, index - 1, followeeId))

        heapq.heapify(heap)

        while heap and len(result) < 10:
            timestamp, id, index, followeeId = heapq.heappop(heap)
            result.append(id)
            if index >= 0:
                timestamp, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(heap, (timestamp, tweetId, index - 1, followeeId))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)

