chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    # Your code here
    merged_list = []
    for i in range(len(chunk_one)):
        merged_list.append(chunk_one[i])
    for i in range(len(chunk_two)):
        merged_list.append(chunk_two[i])
    return merged_list


    
print(merge_list(chunk_one, chunk_two))
