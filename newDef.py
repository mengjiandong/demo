def sum_list(alist):
    sum_temp = 0
    for i in alist:
        sum_temp += 1
    return sum_temp
print(sum_list)
my_list = [23, 45, 67, 89, 100]
my_sum = sum_list(my_list)
print("sum of my list: %d " % (my_sum))