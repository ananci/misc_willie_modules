from willie import module
from willie.module import commands, interval
import subprocess

@commands('supernova')
def supernova(bot, trigger):
    args = trigger.group(2)
    command = 'supernova ' + args

    process = subprocess.Popen(command,shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            )
    #process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    out, err = process.communicate()
    #bot.say('doing stuff')
    process.wait()
    for line in process.stdout:
        bot.say(line)
#    for thing in process.stderr:
#        bot.say(thing)
    #for line in err:
    #    bot.say(err)
    #bot.say('did stuff!')
    #bot.say(out)
#    bot.say(err)
    return module.NOLIMIT
