incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# Your code here
def getFullName(singleObject):
    fullName = singleObject["name"] + " " + singleObject["last_name"]
    return fullName


def data_transformer(list_of_objects):
    list_of_full_names = list(map( getFullName, list_of_objects))
    return list_of_full_names
    
print(data_transformer(incoming_ajax_data))