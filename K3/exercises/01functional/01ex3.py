name_list = ['Loc', 'Anders', 'Jens', 'Henriette', 'Hans Erik', 'Andrea']

# We save the names which are shorter than 4 charactesr OR have s as the last letter in their name. 
result = list(filter(lambda s: len(s) < 4 or s[-1] == 's', name_list))

print(result)