lst = [1, 2]
lst2 = [5, 1]

def comparison(msv, msv2):
    for x in msv:
        if x in msv2:
            print(True)
            break
        else:
            print(False)
            break


comparison(msv=lst, msv2=lst2)