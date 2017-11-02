import flask from Flask
import tweepy

auth = tweepy.OAuthHandler("UphZodN5VxztjNrVSFbHyy0Kj", "Y7lIGuyBOHVxq4mYSDvOm21svJ2YTlBs7pEjnZd1bNIJkYpanD")
auth.set_access_token ("2427229562-5QAWX5pwakcjwLxrpfoyVAf2sISjRM8lWjbnpXy", "hlM8t4ETWbWvidyEINmtQzYnffelN7oUrJ4JkVpGiuY0W")

twitter_api = tweepy.API(auth)
# user = twitter_api.get_user('aleksejstruhans')

for friend in twitter_api.friends_ids("jesskxuan"):
    screen_name = twitter_api.get_user(friend)._json["screen_name"]
    for tweet in tweepy.Cursor(twitter_api.search, q="#metoo" + " from:" + screen_name, rpp=1).items(1):
        if not tweet._json["retweeted"]:
            print screen_name, ": ", tweet._json["text"]
