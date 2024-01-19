lst = [5, 4, 3, 2, 1]
lst2 = []

def index(msv, msv2):
    for num in msv:
        ind = lst.index(num)
        result = num + ind
        lst2.append(result)
    print(msv2)


index(msv=lst, msv2=lst2)