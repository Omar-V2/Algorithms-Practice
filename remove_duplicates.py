def remove_duplicates(a):
    seen = {}
    ans = []
    for n in a:
        if n not in seen:
            seen[n] = 1
            ans.append(n)
    return ans

def remove_duplicates_cs(a):
    vacant = 0
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            vacant +=1 
            a[vacant] = a[i+1]
            print(a)
    return a[:vacant+1]


        
a = [0,0,1,1,1,2,2,3,3,4]
a = remove_duplicates_cs(a)
print(a)


    
