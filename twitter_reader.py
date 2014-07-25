from willie import module
#import twitter

import tweepy

# These keys are gotten from the twitter dev site
# https://dev.twitter.com/
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


def twits(uid):
    """
    @summary: Returns a list of public tweets from a specific uid
    @param uid: The user name or id of the user whos public tweets you would
                like to see
    @type user: String
    @return: List of the most recent public tweets from the uid
    @rtype: List
    """
    # Authenticate and setup the API connection
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Get the most recent tweets from the uid
    public_tweets = api.user_timeline(uid)
    tweets = []

    # Print the tweets one at a time
    for tweet in public_tweets:
        # Sometimes tweets cannot be printed due to
        # encoding or embedded images so let's catch
        # any such tweets and let the bot user know
        try:
            txt_tweet = str(tweet.text)
            tweets.append(txt_tweet)
        except:
            print 'I found a tweet but was unable to display it'
    return tweets


@module.commands('twitter')
def birdie(bot, trigger):
    # Get the twitter uid from the command
    user = trigger.group(2)

    # Tell the bot user that we are pulling tweets
    bot.reply("Fetching Tweets for " + user)
    bot.say("~~~~~~~~***~~~~~~~~")
    print '**' + user + '**'

    # fetch the tweets
    tweets = twits(user)

    # output the tweets, one at a time, to the channel
    for tweet in tweets:
        bot.say(tweet)

    # Let everyone in the channel know we are done
    bot.say("done!")
    bot.say("~~~~~~~~***~~~~~~~~")
