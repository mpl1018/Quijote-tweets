try:
    import json
except ImportError:
    import simplejson as json

import tweepy
import time 

ACCESS_TOKEN = '1183121318105026561-1bPX8ifYnH0pMEr0BTDn13yqZilRto'
ACCESS_SECRET = 'n9SYQS7qIKPS5SfSAmRVIszbytorFAA4nouczccOaBZK2'
CONSUMER_KEY = 'UA4pkzsnngBq1c2hv1yMNGfXR'
CONSUMER_SECRET = 'seDWCTRQhWtOv74tNuae1eH43OCzbLVnUXgkNMLoxf5zrzKnun'

def OAuth(): 
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        return auth 
    

oauth = OAuth()
api = tweepy.API(oauth)

api.update_status('Posting this with python')
