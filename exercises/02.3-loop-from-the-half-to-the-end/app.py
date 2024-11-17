my_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]

# Your code here
initial_value = int(len(my_list)/2)
stop_value = len(my_list)
increase_value = 1

for i in range(initial_value, stop_value, increase_value):
    print(my_list[i])
