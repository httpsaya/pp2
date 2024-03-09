def all_true(tuple_values):
    return all(tuple_values)

tuple_values1 = (True, True, True)
print(all_true(tuple_values1))  

tuple_values2 = (True, False, True)
print(all_true(tuple_values2))  
