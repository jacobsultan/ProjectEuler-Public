"""min = 0, max = len(array)"""

def binsearch(array,target,min,max):
    length = len(array)
    if length == 1:
        return array[0] == target
    elif min == max:
        return array[min] == target

    next = (min + max) / 2
    if array[next] > target:
        binsearch(array,target,min,next)
    else:
        binsearch(array,target,next,max)


