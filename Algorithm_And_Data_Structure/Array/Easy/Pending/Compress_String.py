<<<<<<< HEAD
'''
Created on Jun 28, 2018

@author: USOMZIA
'''
def comprString(s):
    #AAAAAB
    cnt = len(s)
    j = 1
    for i in range(cnt):
        while s[i] == s[i+1]:
            sTemp = s[i] + str(j+1)
            j +=1
        sMain = sMain + sTemp
        i = j
    return sMain
s = "AAAAAAB"
=======
'''
Created on Jun 28, 2018

@author: USOMZIA
'''
def comprString(s):
    #AAAAAB
    cnt = len(s)
    j = 1
    for i in range(cnt):
        while s[i] == s[i+1]:
            sTemp = s[i] + str(j+1)
            j +=1
        sMain = sMain + sTemp
        i = j
    return sMain
s = "AAAAAAB"
>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
pcompr                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     