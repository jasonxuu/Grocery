def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        llist = alist[:mid]
        rlist = alist[mid:]

        llist = merge_sort(llist)
        rlist = merge_sort(rlist)
        
        i, j , k = 0, 0 ,0
        
        while i < len(llist) and j < len(rlist):
            if llist[i] < rlist[j]:
                alist[k] = llist[i]
                i += 1
                k += 1
            else:
                alist[k] = rlist[j]
                j += 1
                k += 1
            
        while i < len(llist):
            alist[k] = llist[i]
            i += 1
            k += 1

        while j < len(rlist):
            alist[k] = rlist[j]
            j += 1
            k += 1
    return alist