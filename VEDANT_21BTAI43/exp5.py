def most_frequent(ch):
    s = set(ch)
    l = list(s)
    d = {}
    i,j = 0,0
    while(i>=0 and i<len(l)):
        j=0
        count = 0 
        while(j>=0 and j<len(ch)):
            if l[i] == ch[j]:
                count +=1
            j+=1
        d.update({l[i]:count})
        i+=1
    print(d)

most_frequent('Mississippi')
