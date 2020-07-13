########
## TASK: to convert List of Tuples into List of Dictionaries.




## Original Data: List of Tuples.
r = [('Aditya', 'Elli'), ('Aditya', 'Spot'), ('Aman', None), ('Anthony', 'Brian'), ('Anthony', 'june')]


# x = {}

# def list_to_dict(r):
#     for result in r:
#         if result[1]:
#             x = {"name":result[0],"pet":result[1]}
    # print(x)

# ************************************************
## For less number of columns this can work.

keys = ['name','pets']
final = []

for result in r:
    for i in range(1):
        inner_result = {}
        inner_result['name']  = result[i]
        inner_result['pets'] = result[i+1]
    final.append(inner_result)


print(final)




# list_to_dict(r)