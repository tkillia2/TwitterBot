# TwitterBot
Twitter Bot created that has been used to annoy friends through retweets, favorites, replies, and direct messages. Working on possible automation as well as creation of own tweets or more.

UPDATE:
Twitter Bot has the initial portion to bother friends commented out and now features the ability to pull Crypto prices and post them, as well as replying to people who are curious of their prices

Have automation in the form of a cronjob that is shown in cronjob.txt --> would be nice to find a server or host for this so that it will run when my computer is turned off

Also have removed the error with duplicate tweets using try/except -- and have added functionality where it will repsond to people with prices for Bitcoin --> can easily be done for other Cryptos

Cronjob for this bot has been removed and a heroku app has been created utilizing a time.sleep(900) function to run every fifteen minutes

Hoping this reamins successful so that it can be used for later purposes as well

Bot currently will only tweet 4 crypto prices currently -- I was consistenly flagged and limited when replying, retweeting, or favoriting tweets, therefore I will most likely have it stay as a crypto pricing bot

the getting-started-python directory was heroku's guide to setting up a heroku app -- there was a lot of difficulty involved in this. I can only get it to work when deploying from my terminal and not from the heroku site

Bots Handle: @CryptoPricing
