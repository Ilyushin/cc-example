import twitter,os,sys,urllib3

urllib3.disable_warnings()

if len(sys.argv) == 2:
#     path_tweets = os.path.abspath(sys.argv[1])
    
    api = twitter.Api(consumer_key='A5jpPSXAZobgq4tzrS24eGnBO',
                          consumer_secret='ihFt9YajphCHWzMd8osvds8l1sbihpbix8Um9aSCq6iEAspCJr',
                          access_token_key='86661745-D3RP99dTIp33zXLb1OM1r4Jkd9kfYuQtTege1ERkV',
                          access_token_secret='X9ro90SimdkIaVSC6a6454fDg0NKWomA3eaaFxsIpQtpB')
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []
    
    new_tweets = api.GetHomeTimeline(count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
        
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    path_tweets = '/Users/Evgeniy/git/cc-example/tweet_input/tweets.txt'
        
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
                
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.GetHomeTimeline(count=200,max_id=oldest)
            
        #save most recent tweets
        alltweets.extend(new_tweets)
            
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
    
    if os.path.exists(path_tweets):
        file_tweets = open (path_tweets, "w")
        for tweet in alltweets:           
            file_tweets.write(str(tweet.text.encode('ascii', 'ignore')))
    
        file_tweets.close()
            