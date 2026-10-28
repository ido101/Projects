s = "EXPECTOPATRONUM"
ABC =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DABC = "KXVZSNOPHABCYMIJQTLEGWRUFD"
def decrypt(s):
    res = ""
    for i in s:
        ind = ABC.index(i)
        res += DABC[ind]
    print(res)

def revers(s):
    res = ""
    for i in s:
        ind = DABC.index(i)
        res += ABC[ind]
    print(res)

decrypt(s) #Didnt work
revers(s) # Success