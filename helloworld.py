from willie import module
import time

@module.commands('helloworld')
def helloworld(bot, trigger):
    bot.reply('Hello world!')

@module.rule('H|hola!?')
def hellopartner(bot, trigger):
    bot.say('Hola, ' + trigger.nick)

@module.commands('echo')
def ZOMGechoBBQ(bot, trigger):
   bot.reply(trigger.group(2))

@module.rule('T|time')
def clocker(bot, trigger):
   local_time = time.asctime(time.localtime(time.time()))
   bot.reply('The clock on the server says ' + local_time + '.')

@module.commands('piglatin')
def piglatin(bot, trigger):
   original_text = trigger.group(2)
   word_list = original_text.split()
   new_text = ""
   for word in word_list:
       new_text = new_text + ' ' + piglatinizer(word)
   bot.reply(new_text)


def piglatinizer(word):
    if(len(word) < 3) or (word == 'the') or (word == 'and'):
        return word
    else:
        if (word[0] in "aeiou") or (word[0] in "AEIOU"):
            new_word = word[1:] + 'way'
        else: 
            new_word = word[1:] + word[0] + 'ay'
	return new_word










