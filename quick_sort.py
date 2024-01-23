def sirt(array,low,high):
    pivot = array[low]
    i = low
    j = high
    while i<j:
        while array[i]<pivot:
            i+=1
        while array[j]>=pivot:
            j-=1
        array[i],array[j]=array[j],array[i]

    array[low], array[j] = array[j], array[low]
    return j


def sorting(li,low,high):
    #find pivot
    #compare all elements in respect to pivot

    pivot = sirt(li,low,high)
    sirt(li,low,pivot-1)
    sirt(li,pivot+1,high)
    return li



array = [2,6,1,5,7,3]
sorting(array,0,len(array)-1)