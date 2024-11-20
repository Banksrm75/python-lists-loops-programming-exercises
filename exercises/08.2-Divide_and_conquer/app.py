list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

def sort_odd_even(list_of_numbers):
    sorted_list = []
    even = []
    for i in range (len(list_of_numbers)):
        if list_of_numbers[i] % 2 != 0:
            sorted_list.append(list_of_numbers[i])
        else:
            even.append(list_of_numbers[i])
    for i in range (len(even)):
        sorted_list.append(even[i])
    return sorted_list


print(sort_odd_even(list_of_numbers))

