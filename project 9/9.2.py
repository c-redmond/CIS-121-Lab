num_1 = int(input())
num_2 = 5
num_3 = 25
num_2 = int(input())
num_3 = int(input())
def ascending_order():
    num_list = []
    num_list.append(num_1)
    num_list.appen(num_2)
    num_list.appen(num_3)
    largest = 0
    middle = 0
    smallest = 0
    for num in num_list:
        if num >= largest:
            largest = num
        if num <= smallest:
            smallest = num
        else:
            middle = num
    sorted_list = [smallest, middle, largest]
    return sorted_list
print(int(ascending_order(num_1, num_2, num_3)))