import bot

CONSUMER_KEY = "xdkZZN8IuKiyYTzpdWIJapq"
CONSUMER_SECRET = "v7FpihZuZcFqyWIJGYtRskVxE7dlAAvvUZThj8psJlFwKU5r"
ACCESS_KEY = "1132206744-tPWrPoap39jYEEpx2H0LTrmP2gMdMqhUe6hQA"
ACCESS_SECRET ="E0We2WgAJkUewJDSjyUNC4BG8QuATqGdhNn9VuUMYEO"

api = bot.get_api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# load tweet and pic
tw = []
pic = []

bot.load_tw(tw)
bot.load_pic(pic)

# 11:27am
#bot.specific_time_tweet(api, tw, pic, 16, 43, rand=1)
bot.specific_day_tweet(api, tw, pic, 4, 16, 46, rand=1)
