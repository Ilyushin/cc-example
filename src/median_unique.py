import numpy


def calculate_median(data, path_ft2):
   
    arr_median_number = []
    arr_unic_words = [] 
    
    #calculate the median number of unique words per tweet      
    for tweet in data:        
        arr_unic_words.append(len(set(tweet.lower().split(' '))))             
        arr_median_number.append([tweet, numpy.median(arr_unic_words)])
    
    #save result in the file   
    if len(arr_median_number) > 0:
        file_ft2 = open(path_ft2, 'w')
        file_ft2.truncate(0) 
        for item in arr_median_number:
            file_ft2.write(str(item[1])+"\n")            
        file_ft2.close()
    