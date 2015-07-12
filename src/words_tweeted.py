def calculate_words(data,path_ft1):       
    #create dictionary that consist of 
    #key = word and value = number of times each word has been tweeted 
    dict_words = {}
    #max_len_word = 0
    for tweet in data:
        words = tweet.lower().split()               
        for w in words:
            word = w.strip()        
            dict_words.setdefault(word,0)
            dict_words[word] += 1 
            #max_len_word = len(w) if max_len_word < len(w) else max_len_word 

    #save words and their number of times in the file
    #We can print as shown below, but this way degrades performance 
    #and makes bigger the file of result. 
    #It is important when we analyse a lot of tweets.
    #word1   3
    #word2   1
    #word3   3
    if len(dict_words) > 0:
        file_ft1 = open(path_ft1, 'w')
        file_ft1.truncate(0) 
        for key in sorted(dict_words):
            #file_ft1.write(str(key)+str(' '*(max_len_word-len(key))+'      ')+str(dict_words[key]))              
            file_ft1.write(str(key)+str('   ')+str(dict_words[key])+"\n")             
        file_ft1.close()
    
