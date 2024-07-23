def longdivision(top,bottom):
    arr = [top]
    ind = 0
    while(ind < 100):                      
        curr = arr[ind]        
        if curr == 0:
            break
        elif bottom > curr:
            arr.append(curr * 10)
            arr[ind] = 0
        else:
            place = int(curr / bottom)
            arr[ind] = place
            arr.append( (curr - arr[ind] * bottom) * 10)
            
        ind += 1
    return arr