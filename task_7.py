lst = [1, 2, 3, 5, 53, "Hello world", "hello", "12321", 1, 2, 3.1]
lst2 = []

def only_integer(msv, msv2):
    for num in msv:
        if type(num) == float:
            lst.remove(num)

        if type(num) == int:
            lst2.append(num)
    print(msv2)

only_integer(msv=lst, msv2=lst2)