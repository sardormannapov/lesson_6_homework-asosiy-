inp = int(input("Enter num: "))
lst = [5, 6, 7, 8, 9]

def next_in_line(input, msv):
    del lst[0]
    lst.append(input)
    print(msv)


next_in_line(input=inp, msv=lst)