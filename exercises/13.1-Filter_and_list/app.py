all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here

def names_starting_with_R(name):
   return name.startswith("R")

resulting_names = list(filter(names_starting_with_R, all_names))
print(resulting_names)




