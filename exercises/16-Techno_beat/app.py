def lyrics_generator(list):
    lyrics = []
    count = 0
    for i in range(len(list)):
        if (list[i] == 0):
            lyrics.append("Boom")
            count = 0
        elif (list[i] == 1):
            if count < 2:
                lyrics.append("Drop the bass")
                count += 1
            else:
                lyrics.append("Drop the bass !!!Break the bass!!!")
                count = 0
    return lyrics




# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
