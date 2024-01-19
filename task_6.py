lst = [1, 1]
lst2 = []

def clone(msv, msv2):
    clon = lst.copy()
    lst2.append(msv)
    lst2.append(clon)
    print(msv2)

clone(msv=lst, msv2=lst2)