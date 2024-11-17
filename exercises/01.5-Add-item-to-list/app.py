# Remember to import random function here
import random

my_list = [4, 5, 734, 43, 45]

# The magic goes below
for i in range(10):
    my_num = random.randint(0, 800)
    my_list.append(my_num)

print(my_list)
