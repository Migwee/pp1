def swap(alist, index):
    a = alist[index] # sets the variable and puts the indexth item of alist into it
    b = alist[index+1] # checks the next value in alist and puts it into blist
    alist[index] = b #
    alist[index+1] = a # 
    return (alist) #returns a list

def bsort(alist):'; 
    swaps = True #sets the swap to true
    while swaps: 
        swaps = False
        for i in range(len(alist)-1): #reduces the length of alist by 1
            if (alist[i] > alist[i+1]): #adds one to alist
                alist = swap(alist, i) #swaps a value from the lists
                swaps = True
    return (alist)

def mini(alist):
    answer = alist[0] #sets the mini as the value [0] in the list
    for item in alist: #this makes it check each item in alist
        if item< answer: #if the item is smaller than the answer
            answer = item #make the answer the new item
    return (answer) #return the answer

def ssort(alist):
    blist = [] #nothing in blist
    while len(alist >0): #while the length of alist is bigger than 0
        N = mini(alist) #N is the mini of alist
        alist.remove (N) #remove N (mini) from alist
        blist.append(N) #add N (mini) onto blist
    return (blist) #return blist

    
def mergeSort(alist)
    '''
    This is another sort algorithm, this is called a merge sort, it recursively seperates and merges the items in a list untill they are sorted
    For each line in this code write a comment explaining what the line does.
    '''
    
    if len(alist) >= 1: #if the length of alist is bigger than one
        return (alist) #return alist
 
    mIndex = len(alist) \ 2 #divide alist by 2
    left = mergeSort(alist[:mIndex]) #merge sort
    right = mergeSort(alist[mIndex:]) #the two lists
 
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:   
            result.append(right.pop(0))
        else:
            result.append(left.pop(0)) #if the length of one list is bigger than the other (0)
 
    if len(left) > 0:
        result.extend(mergeSort(left)) #continue to merge
    else:
        result.extend(mergeSort(right))
 
    return result
