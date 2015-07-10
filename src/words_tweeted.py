def calculate_words(data,path_ft1):       
    #create dictionary that consist of 
    #key = word and value = number of times each word has been tweeted. 
    dict_words = {}
    for tweet in data:
        words = tweet.lower().split()               
        for w in words:
            word = w.strip()        
            dict_words.setdefault(word,0)
            dict_words[word] += 1   

    #save words and their number of times in the file.
    if len(dict_words) > 0:
        file_ft1 = open(path_ft1, 'w')
        file_ft1.truncate(0) 
        for key in sorted(dict_words):              
            file_ft1.write(str(key)+str('   ')+str(dict_words[key])+"\n")             
        file_ft1.close()
    