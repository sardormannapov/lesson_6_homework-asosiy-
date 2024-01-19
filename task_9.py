x = int(input("enter first_parametr :"))
y = int(input("enter second_parametr :"))
n = int(input("enter third_parametr :"))
list = []

def find_divisible_num(first,second,third,lst):
    for numbers in range(first,second + 1):
        if numbers % third == 0:
            lst.append(numbers)
    print(lst)


print(find_divisible_num(x,y,n,list))