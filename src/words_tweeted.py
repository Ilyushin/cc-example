import sys,os

print len(sys.argv)
if len(sys.argv) == 3:
    path_tweets = os.path.abspath(sys.argv[1])
    path_ft1 = os.path.abspath(sys.argv[2])
    print path_tweets
    print path_ft1    
    dict_words = {}
    max_len_word = 0    
 
# path_tweets = '/Users/Evgeniy/git/cc-example/tweet_input/tweets.txt'
# path_ft1 = '/Users/Evgeniy/git/cc-example/tweet_output/ft1.txt'    
# dict_words = {}
# max_len_word = 0
    
    data = []
    if os.path.exists(path_tweets):
        with open (path_tweets, "r") as file_tweets:
            data = file_tweets.read().encode('ascii', 'ignore').split('\n')   

    for i,j in enumerate(data):
        words = j.lower().split(' ')
        for w in words:
            dict_words.setdefault(w,0)
            dict_words[w] = dict_words[w]+1
            if max_len_word < len(w):
                max_len_word = len(w)
        

    if len(dict_words) > 0:
        file_ft1 = open(path_ft1, 'w')
        file_ft1.truncate(0) 
        for key in sorted(dict_words):  
            file_ft1.write(str(key)+str(' '*(max_len_word-len(key))+' ')+str(dict_words[key]))       
            file_ft1.write("\n")
        file_ft1.close()