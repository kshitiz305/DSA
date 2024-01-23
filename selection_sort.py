def selection_sort(array):
    for position in range(len(array)-1):
        minimium = currentpos = position+1

        for replace in range(currentpos,len(array)):
            if array[replace] < array[minimium]:
                minimium = replace
        array[position] ,array[minimium] = array[minimium] ,array[position]
    return array


print(selection_sort([33,55,66,22,11,44]))


#
# timecomplexity = n^2
# https://youtu.be/ee80YmiaSVQ?si=t7kgMBfvN6lv4ToA
