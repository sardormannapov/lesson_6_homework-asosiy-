lst = ["sardor"]
ln = len(lst)

def online(msv, size):

    if size == 0:
        print("no online")

    elif size == 1:
        print(msv[0] + " online")

    elif ln == 2:
        print(f"{msv[0]} and {msv[1]}" + " online")

    else:
        print("salam aleykum")

online(msv=lst, size=ln)