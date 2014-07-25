import feedparser
from willie import module


@module.commands('subreddit')
def feeder(bot, trigger):
    # get the subreddit that was passed to the command
    subreddit = trigger.group(2)
    bot.say("Now getting top 5 posts from r/" + subreddit)

    # using feedparser, get the submisions to that subreddit, this will
    # return a list of dicts
    d = feedparser.parse('http://www.reddit.com/r/' + subreddit + '/.rss')

    # print out the top 5 submissions in that subreddit
    for x in range(5):
        bot.say(d['entries'][x]['title'] + ": " + d['entries'][x]['link'])
