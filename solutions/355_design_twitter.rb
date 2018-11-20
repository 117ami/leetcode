# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:
# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
# Example:
# Twitter twitter = new Twitter();
# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);
# // User 1 follows user 2.
# twitter.follow(1, 2);
# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.getNewsFeed(1);
# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);
#
#  https://leetcode.com/problems/design-twitter/description/
require './aux.rb'

class Twitter
  #     Initialize your data structure here.
  def initialize
    @alltweets = []
    @follows = {}
  end

  #     Compose a new tweet.
  #     :type user_id: Integer
  #     :type tweet_id: Integer
  #     :rtype: Void
  def post_tweet(user_id, tweet_id)
    @alltweets << [user_id, tweet_id]
  end

  #     Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
  #     :type user_id: Integer
  #     :rtype: Integer[]
  def get_news_feed(user_id)
    ids = []
    @follows[user_id] = { user_id => 1 } unless @follows.key?(user_id)
    @alltweets.reverse_each do |uid, tid|
      ids << tid if uid == user_id || @follows[user_id][uid]
      return ids if ids.size >= 10 
    end
    ids
  end

  #     Follower follows a followee. If the operation is invalid, it should be a no-op.
  #     :type follower_id: Integer
  #     :type followee_id: Integer
  #     :rtype: Void
  def follow(user_id, followee_id)
    @follows[user_id] = { user_id => 1 } unless @follows.key?(user_id)
    @follows[user_id][followee_id] = 1
  end

  #     Follower unfollows a followee. If the operation is invalid, it should be a no-op.
  #     :type follower_id: Integer
  #     :type followee_id: Integer
  #     :rtype: Void
  def unfollow(user_id, followee_id)
    @follows[user_id] = { user_id => 1 } unless @follows.key?(user_id)
    @follows[user_id][followee_id] = nil
   end
end

# Your Twitter object will be instantiated and called as such:
obj = Twitter.new
[11,22,333,505,94,2,10,13,101,3,5].reverse_each.each do |tid|
obj.post_tweet(1, tid)
end 
# obj.post_tweet(1, 7)
param_2 = obj.get_news_feed(1)
p param_2
obj.follow(1, 2)
# obj.unfollow(1, 2)
obj.post_tweet(2, 4)
p obj.get_news_feed(1)
