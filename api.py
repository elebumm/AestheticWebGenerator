import requests
import settings
import random
import json
import twitter
import re


# strings and booleans for plain web links
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
url = "http://api.giphy.com/v1/gifs/random?"
flag = False

# GIPHY api key
api_key = settings.giphy_api


# variables for twitter api
api = twitter.Api(consumer_key=settings.consumer_key,
                  consumer_secret=settings.consumer_secret,
                  access_token_key=settings.access_key,
                  access_token_secret=settings.access_secret)
rt_search = re.compile(r'\brt\b')
ment_search = re.compile(r'\B@[a-z0-9_-]+')


# grabs a random word from the freebsd.org dictionary. Then decodes byte to a string.
# b'hilarious' -> hilarious
def get_random_query():
    r = requests.get(word_site)
    words = r.content.splitlines()
    random_word = random.choice(words).decode('utf-8')
    random_query = url + "&api_key=" + api_key + '&tag=' + random_word
    print('Your website theme is: ' + random_word)
    # Returns a tuple so that you can get the random query as well the random word in case you wanted the theme.
    return random_query, random_word


# the url response will reply with json. we import the json library to parse and grab the url for the image.
def get_image_link(link):
    global flag
    r = requests.get(link)
    api_response = json.loads(r.text)
    response = api_response['data']
    if not response:
        print('No GIFS for this theme :(... rerunning application')
    elif response:
        flag = True
        return response['image_original_url']


# uses twitter api to grab random tweets that use the random_word variable. This replaces lorem ipsum
def get_tweet(random_word):
    result_store = []
    i = 0
    t_set = 0
    print('Checking Twitter API... this may take a moment...')
    try:
        while i < 5:
            results = str(api.GetSearch(raw_query='q=' + random_word + '&count=200&replies=none&retweets=none')[t_set])
            api_response = json.loads(results)
            if rt_search.search(api_response['text'].lower()) is None:
                if ment_search.search(api_response['text'].lower()) is None:
                    print('Tweet grabbed! request made: ' + str(t_set + 1))
                    result_store.append(api_response['text'])
                    i += 1
                    t_set += 1
                pass
            else:
                print('trying again. Request made: ' + str(t_set + 1))
                t_set += 1
                pass
        print('Requests total: ' + str(t_set + 1) + '/180')
        return result_store
    except twitter.error.TwitterError:
        print('Exceeded Twitter API use... (180 requests per 15 minutes) ')
        exit()
