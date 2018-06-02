import csv
import time
import tweepy


########## ~ Careful of overwrites ~ ############

accountvar = "paulg"

##############################################

consumer_key = "YOUR KEY #1 GOES HERE"
consumer_secret = "YOUR KEY #2 GOES HERE"
access_key = "YOUR KEY #3 GOES HERE"
access_secret = "YOUR KEY #4 GOES HERE"

##############################################

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

print "Searching for followers of " + accountvar

users = tweepy.Cursor(api.followers, screen_name=accountvar, count=200).items()

count = 0
errorCount = 0

outputfilecsv = accountvar + " followers.csv" # Note: this will overwrite if you run this program more than once for the same username
fc = csv.writer(open(outputfilecsv, 'wb'))
fc.writerow(["Name", "Account Name", "ID", "Verified", "Description", "Followers Count", "Statuses Count","Location","Time Zone", "Language", "Following You", "Site URL", "Twitter URL"])

while True:
    try:
        user = next(users)
        count += 1
        if count % 1000 == 0:
            print("Count is: " + str(count))
                                # You can use count-break during dev to avoid twitter restrictions

    except StopIteration:       # May be redundant
        break

    try:
        twit_url = "twitter.com/" + user.screen_name.encode('UTF-8')
        fc.writerow([
            user.name.encode('UTF-8'),
            user.screen_name.encode('UTF-8'),
            user.id_str, user.verified,
            user.description.encode('UTF-8'),
            str(user.followers_count),
            str(user.statuses_count),
            user.location.encode('UTF-8'),
            user.time_zone,
            user.lang.title(),
            user.following,
            user.url,
            twit_url])

    except UnicodeEncodeError:
        errorCount += 1
        print "Unicode Error"

print "Completed. Error Count = " + str(errorCount) + "; Total Users = " + str(count)


"""
Full credit to mataxu on StackOverflow for the inspiration & the bulk of the work on this
http://stackoverflow.com/questions/31000178/how-to-get-large-list-of-followers-tweepy

Main API reference: http://docs.tweepy.org/en/v3.2.0/api.html#API
"""
