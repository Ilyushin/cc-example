import sys,os,threading,words_tweeted, median_unique

if len(sys.argv) == 4:
    #set parameters
    path_tweets = os.path.abspath(sys.argv[1])
    path_ft1 = os.path.abspath(sys.argv[2])
    path_ft2 = os.path.abspath(sys.argv[3]) 
    
    #read tweets from the file
    data = []
    if os.path.exists(path_tweets):
        with open (path_tweets, "r") as file_tweets:
            data = file_tweets.read().split('\n')
            try:
                data.remove('')
            except:
                pass
            
    threading.Thread(target=words_tweeted.calculate_words, args=(data,path_ft1)).start()    
    threading.Thread(target=median_unique.calculate_median, args=(data, path_ft2)).start()


