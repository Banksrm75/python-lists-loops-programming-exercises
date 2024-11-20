my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

def max_integer(list):
    largest_so_far = (list[0])
    for i in range(len(list)):
        if list[i] > (largest_so_far):
            largest_so_far = list[i]
    return largest_so_far

print(max_integer(my_list))
