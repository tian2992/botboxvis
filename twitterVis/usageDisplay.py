import tweepy
import os

auth = None # bad habits are hard to kill
consumer_key = "uxFUGLPgtTcpWC7TahiWiQ"
consumer_secret = "ubSEKXxXMFtVbvyHfoZ2DIAjfPI8sSJ2TvukaGDvSjE"
filename = "auth_tokens.txt"
sinceID = "33510331653292033" #first feburary twitt

if os.path.exists(filename):
  token_file = open(filename, "r", 0)
  user_key = token_file.readline().rstrip()
  user_secret = token_file.readline().rstrip()
  token_file.close()
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(user_key, user_secret)
else:
  token_file = open(filename, "w", 0)
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  # Redirect user to Twitter to authorize
  try:
      redirect_url = auth.get_authorization_url()
      print ("To allow access, visit: "+ redirect_url)
  except tweepy.TweepError:
      print ('Error! Failed to get request token.')
  # Example w/o callback (desktop)
  verifier = raw_input('Verifier:')
  # Get access token
  auth.get_access_token(verifier)
  token_file.writelines(auth.access_token.key+"\n")
  token_file.writelines(auth.access_token.secret+"\n")
  token_file.close()


api = tweepy.API(auth)

allStatus = api.list_timeline("tian2992", "usac-ecys",since_id=sinceID, per_page=500)

weekdays_sum = 0.0
resultsSize = 0 # because allStatus.count() doesn't work

for status in allStatus:
  weekdays_sum = weekdays_sum + status.created_at.weekday()
  resultsSize = resultsSize + 1
  #print (status.id_str+" --- "+status.created_at.isoformat())
  #print (status.text)
  
print ("Average Weekday for Tweets: "+str(weekdays_sum/resultsSize))
