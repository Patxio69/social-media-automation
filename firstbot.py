import tweepy

consumer_key=""
consumer_secret=""
Access_key="923299188938592256-0ZKg0lg5PNLG7MlIQ9DHID7OgqWfJgr"
Access_secret="Mxg6TSfrSbx6mFN6x7ZXblzcPgoLYn4L1I9LJHT9UC5oq"

any_varname = tweepy.OAuthHandler(consumer_key, consumer_secret) #tweet module name.Outhstuff(cons_key, secret_key)
any_varname.get_access_token(Access_key, Access_secret)
api = tweepy.API(auth)

