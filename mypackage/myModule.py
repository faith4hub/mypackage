def top_n(items, n):
    ''' Return the top n items in an array, in desc order
    
    Args:
        items (array): list or array-like object
        n (int): num of items to return
        
        For statement:
        n(int): this also tells how many passes/ bubble-sort need to be done. it goes through each element
        in items, warming up to the for statement. till the largest item is place at the end of the list.
        
        It checks each neighboring number and swaps places if needed. 
        So, it goes through all the elements until it reaches the end of the line.
        if n=2, it goes over the list (items) the second time, excluding the biggest elmemnt from the first pass
        likewise if n=3 or 4,5, etc.
        
        tip: 
        add ,items to Return to see how bubble-sort works.
            
    Return:
        array: top n items, in desc order
        
    Egs:
        >>> top_n ([8,3,2,7,4], 3)
        [8,7,4]
        
    ''' 
    for i in range(n): #keep sorting until we have the top n items
        for j in range(len(items)-1-i):
            
            if items[j] > items[j+1]: # if this is bigger than the next line
                items[j], items[j+1] = items[j+1], items[j] #swap the two
                
    
    # sorted item {which is items} with reverse indexing
    #-n: The negative index -n means counting from the end of the list
    top_n = items[-n:]
    
    #return in descending order
    return top_n[::-1]
    
    # or comment top_n in line 24 and return items[::-1]
    