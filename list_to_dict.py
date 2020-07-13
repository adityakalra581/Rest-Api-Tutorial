r = [('Aditya', 'Elli'), ('Aditya', 'Spot'), ('Aman', None), ('Anthony', 'Brian'), ('Anthony', 'june')]


x = {}

def list_to_dict(r):
    for result in r:
        if result[1]:
            x = {"name":result[0],"pet":result[1]}
    print(x)


list_to_dict(r)