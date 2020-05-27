#Given two lists of integer (list and sequence) print the sortest sequence of elements
#from list that contains all the elements from the sequence

def dcp(list, sequence):
    fans = []
    for i in range(len(list)):
        tmp = sequence.copy()
        ans = []
        if list[i] in sequence:
            tmp.remove(list[i])
            ans.append(list[i])
            for j in range(i+1, len(list)):
                ans.append(list[j])
                if list[j] in tmp:
                    tmp.remove(list[j])
                if not tmp:
                    if len(ans) < len(fans):
                        fans = ans
                    if not fans:
                        fans = ans
                    break

    return fans
