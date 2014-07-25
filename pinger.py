from willie import module
import subprocess

@module.commands('ping')
def pinger(bot, trigger):
    address = trigger.group(2)

    # this is the command we want to run
    # my bot is running on a linux computer, so
    # the ping command is different than it would
    # be for bots running on windows or macs
    command = 'ping -c 1 ' + address

    # In order to run a 'command line' or 'terminal'
    # command in python we're going to use the
    # subprocess module. This let's us safely
    # (well more safely than other methods) run
    # a command from python. Please note - for
    # security reasons you should do careful parsing
    # of anything a user passes in. With this code,
    # as is, a user could potentially do much more
    # than 'ping'!
    process = subprocess.Popen(command,
                               shell=True,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               )
    # Wait for the command to be done
    process.wait()

    # make an empty list to hold our results
    result = []

    # for every line that the program returned, put that line in the
    # results list. We are doing this to avoid having to parse anything
    # later. It is a little hacky
    for line in process.stdout:
        result.append(line)

    # uncomment the next line to see, in terminal, what the results are
    #print result

    # This works because we know what the command will output.
    # We want the original ping response, and we want the result of the
    # ping. Everything else is just extra and kind of spammy. Since we
    # know exactly what it will look like we're going to be a little hacky
    # here too:
    # The bot should reply with the original ping command response
    bot.reply(result[0])

    # the lenght of the result list will only be greater than two if the
    # ping was successful. If it was we want to know what that final result
    # was so the bot should reply. Otherwise(if the ping failed) there's
    # nothing useful here
    if len(result) > 2:
        bot.reply(result[1])

    # This allows the user to, once the command has been completed, immediately
    # make another request. This should be changed and another decorator should
    # be added if you are worried about a user spamming this in a channel
    return module.NOLIMIT
