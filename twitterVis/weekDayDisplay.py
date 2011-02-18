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

day_values = [0,0,0,0,0,0,0]
week_day = 0

for status in allStatus:
  week_day = status.created_at.weekday()
  day_values[week_day] = day_values[week_day] + 1  

size(640,395)
background(255)

bar_width = 90
margins = 20

max_value = max(day_values)

colormode(HSB)
xpos = 0
ypos = HEIGHT-margins

for (day, value) in enumerate(day_values):
  fill(day/7.0,max_value/value,0.8)
  xpos = (day*bar_width)+margins
  rect(xpos,ypos,bar_width-margins,-value*3)
  fill(0)
  text(unicode(value),xpos,ypos)
