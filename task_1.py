lst = [1, 2, 3, "a", "b", 4]
lst2 = []

def str(msv, msv2):
    for num in msv:
        if type(num) == int:
            lst2.append(num)
    print(msv2)

str(msv=lst, msv2=lst2)