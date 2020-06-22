#This problem was asked by Google.
#Given a word W and a string S, find all starting indices in S which are anagrams of W.
#For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.

def search(text, subtext):
    ltr = []
    for i in range(len(text)):
        if text[i] == subtext[0]:
            k = 0
            check = True
            for j in range(i, i + len(subtext)):
                try:
                    if subtext[k] != text[j]:
                        check = False
                    k = k + 1
                except:
                    check = False
            ltr.append(i) if check else None
        if text[i] == subtext[len(subtext) - 1]:
            k = len(subtext) - 1
            check = True
            for j in range(i, i + len(subtext)):
                try:
                    if subtext[k] != text[j]:
                        check = False
                    k = k - 1
                except:
                    check = False
            ltr.append(i) if check else None
    return ltr