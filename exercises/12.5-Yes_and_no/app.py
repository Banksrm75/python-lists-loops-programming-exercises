the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here
def transform_wikiwoko(bool):
    if bool == 0:
        return 'woko'
    elif bool == 1:
        return 'wiki'
    else:
        return "That is not a boolean!"
print(list(map(transform_wikiwoko, the_bools)))