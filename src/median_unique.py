import sys,os,numpy

if len(sys.argv) == 3:
    path_tweets = os.path.abspath(sys.argv[1])
    path_ft2 = os.path.abspath(sys.argv[2])
        
    data = []
    if os.path.exists(path_tweets):
        with open (path_tweets, "r") as file_tweets:
            data = file_tweets.read().encode('ascii', 'ignore').split('\n')
     
    count_unic_words = 0
    dict_words = {}
    arr_median_number = []
    arr_unic_words = []      
    for i,j in enumerate(data):        
        words = j.lower().split(' ')
        for w in words:
            dict_words.setdefault(w,0)
            dict_words[w] = dict_words[w]+1
            if dict_words[w] == 1:
                count_unic_words = count_unic_words+1        
        arr_unic_words.append(count_unic_words)
        count_unic_words = 0
        dict_words.clear()
        arr_median_number.append([j, numpy.median(arr_unic_words)])
     
    if len(arr_median_number) > 0:
        file_ft2 = open(path_ft2, 'w')
        file_ft2.truncate(0) 
        for item in arr_median_number:
            file_ft2.write(str(item[1]))       
            file_ft2.write("\n")
        file_ft2.close()