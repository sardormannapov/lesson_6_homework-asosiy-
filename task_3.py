inp = int(input("Enter number: "))
lst = [5, 1, 8, 9]
lst2 = []



def percent(input, msv, msv2):
    m1 = len(msv)
    for num in msv:
        if num > input or num == input:
            lst2.append(num)
            m2 = len(msv2)
            result = (m2*100/m1)
        print(result)


percent(input=inp, msv=lst, msv2=lst2)